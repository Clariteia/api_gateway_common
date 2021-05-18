"""
Copyright (C) 2021 Clariteia SL

This file is part of minos framework.

Minos framework can not be copied and/or distributed without the express permission of Clariteia SL.
"""
from __future__ import (
    annotations,
)

import abc
import collections
import os
import typing as t
from pathlib import (
    Path,
)

import yaml

from minos.api_gateway.common.exceptions import (
    MinosConfigDefaultAlreadySetException,
    MinosConfigException,
)

CONNECTION = collections.namedtuple("Connection", "host port")
ENDPOINT = collections.namedtuple("Endpoint", "name route method controller action")
REST = collections.namedtuple("Rest", "connection endpoints")
DISCOVERY_CONNECTION = collections.namedtuple("DiscoveryConnection", "host port path")
DATABASE = collections.namedtuple("Database", "host port password")
DISCOVERY = collections.namedtuple("Discovery", "connection endpoints database")

_ENVIRONMENT_MAPPER = {
    "rest.host": "API_GATEWAY_REST_HOST",
    "rest.port": "API_GATEWAY_REST_PORT",
    "discovery.host": "DISCOVERY_SERVICE_HOST",
    "discovery.port": "DISCOVERY_SERVICE_PORT",
    "discovery.db.host": "DISCOVERY_SERVICE_DB_HOST",
    "discovery.db.port": "DISCOVERY_SERVICE_DB_PORT",
    "discovery.db.password": "DISCOVERY_SERVICE_DB_PASSWORD",
}

_PARAMETERIZED_MAPPER = {
    "rest.host": "api_gateway_rest_host",
    "rest.port": "api_gateway_rest_port",
    "discovery.host": "discovery_service_host",
    "discovery.port": "discovery_service_port",
    "discovery.db.host": "discovery_service_db_host",
    "discovery.db.port": "discovery_service_db_port",
    "discovery.db.password": "discovery_service_db_password",
}

_default: t.Optional[MinosConfigAbstract] = None


class MinosConfigAbstract(abc.ABC):
    """Minos abstract config class."""

    __slots__ = "_services", "_path"

    def __init__(self, path: t.Union[Path, str]):
        if isinstance(path, Path):
            path = str(path)
        self._services = {}
        self._path = path
        self._load(path)

    @abc.abstractmethod
    def _load(self, path: str) -> None:
        raise NotImplementedError  # pragma: no cover

    @abc.abstractmethod
    def _get(self, key: str, **kwargs: t.Any):
        raise NotImplementedError  # pragma: no cover

    @staticmethod
    def _file_exit(path: str) -> bool:
        if os.path.isfile(path):
            return True
        return False

    def __enter__(self) -> MinosConfigAbstract:
        self.set_default(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> t.NoReturn:
        self.unset_default()

    @staticmethod
    def set_default(value: MinosConfigAbstract) -> t.NoReturn:
        """Set default config.

        :param value: Default config.
        :return: This method does not return anything.
        """
        if MinosConfigAbstract.get_default() is not None:
            raise MinosConfigDefaultAlreadySetException("There is already another config set as default.")
        global _default
        _default = value

    @classmethod
    def get_default(cls) -> MinosConfigAbstract:
        """Get default config.

        :return: A ``MinosConfigAbstract`` instance.
        """
        global _default
        return _default

    @staticmethod
    def unset_default() -> t.NoReturn:
        """Unset the default config.

        :return: This method does not return anything.
        """
        global _default
        _default = None


class MinosConfig(MinosConfigAbstract):
    """Minos config class."""

    __slots__ = ("_data", "_with_environment", "_parameterized")

    def __init__(self, path: t.Union[Path, str], with_environment: bool = True, **kwargs):
        super().__init__(path)
        self._with_environment = with_environment
        self._parameterized = kwargs

    def _load(self, path):
        if self._file_exit(path):
            with open(path) as f:
                self._data = yaml.load(f, Loader=yaml.FullLoader)
        else:
            raise MinosConfigException(f"Check if this path: {path} is correct")

    def _get(self, key: str, **kwargs: t.Any) -> t.Any:
        if key in _PARAMETERIZED_MAPPER and _PARAMETERIZED_MAPPER[key] in self._parameterized:
            return self._parameterized[_PARAMETERIZED_MAPPER[key]]

        if self._with_environment and key in _ENVIRONMENT_MAPPER and _ENVIRONMENT_MAPPER[key] in os.environ:
            return os.environ[_ENVIRONMENT_MAPPER[key]]

        def _fn(k: str, data: dict[str, t.Any]) -> t.Any:
            current, _, following = k.partition(".")

            part = data[current]
            if not following:
                return part

            return _fn(following, part)

        return _fn(key, self._data)

    @property
    def rest(self) -> REST:
        """Get the rest config.

        :return: A ``REST`` NamedTuple instance.
        """
        connection = self._rest_connection
        endpoints = self._rest_endpoints
        return REST(connection=connection, endpoints=endpoints)

    @property
    def _rest_connection(self):
        connection = CONNECTION(host=self._get("rest.host"), port=int(self._get("rest.port")))
        return connection

    @property
    def _rest_endpoints(self) -> list[ENDPOINT]:
        info = self._get("rest.endpoints")
        endpoints = [self._rest_endpoints_entry(endpoint) for endpoint in info]
        return endpoints

    @staticmethod
    def _rest_endpoints_entry(endpoint: dict[str, t.Any]) -> ENDPOINT:
        return ENDPOINT(
            name=endpoint["name"],
            route=endpoint["route"],
            method=endpoint["method"].upper(),
            controller=endpoint["controller"],
            action=endpoint["action"],
        )

    @property
    def discovery(self) -> DISCOVERY:
        """Get the rest config.

        :return: A ``REST`` NamedTuple instance.
        """
        connection = self._discovery_connection
        endpoints = self._discovery_endpoints
        database = self._discovery_database
        return DISCOVERY(connection=connection, endpoints=endpoints, database=database)

    @property
    def _discovery_connection(self):
        connection = CONNECTION(host=self._get("discovery.host"), port=int(self._get("discovery.port")))
        return connection

    @property
    def _discovery_database(self):
        connection = DATABASE(
            host=self._get("discovery.db.host"),
            port=int(self._get("discovery.db.port")),
            password=self._get("discovery.db.password"),
        )
        return connection

    @property
    def _discovery_endpoints(self) -> list[ENDPOINT]:
        info = self._get("discovery.endpoints")
        endpoints = [self._discovery_endpoints_entry(endpoint) for endpoint in info]
        return endpoints

    @staticmethod
    def _discovery_endpoints_entry(endpoint: dict[str, t.Any]) -> ENDPOINT:
        return ENDPOINT(
            name=endpoint["name"],
            route=endpoint["route"],
            method=endpoint["method"].upper(),
            controller=endpoint["controller"],
            action=endpoint["action"],
        )
