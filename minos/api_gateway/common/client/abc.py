"""
Copyright (C) 2021 Clariteia SL

This file is part of minos framework.

Minos framework can not be copied and/or distributed without the express permission of Clariteia SL.
"""
from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Any,
)


class ClientHttpBase(ABC):  # pragma: no cover
    """Minos abstract HTTP client class."""

    @abstractmethod
    async def get(self, url, params: dict = None, **kwargs: Any):
        pass

    @abstractmethod
    async def post(self, url, params: dict = None, data: Any = None, **kwargs: Any):
        pass

    @abstractmethod
    async def put(self, url, params: dict = None, data: Any = None, **kwargs: Any):
        pass

    @abstractmethod
    async def patch(self, url, params: dict = None, data: Any = None, **kwargs: Any):
        pass

    @abstractmethod
    async def delete(self, url, params: dict = None, data: Any = None, **kwargs: Any):
        pass

    @staticmethod
    async def _trigger_request(method, url, params, data: Any = None, **kwargs: Any):
        pass
