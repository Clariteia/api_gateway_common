# Copyright (C) 2020 Clariteia SL
#
# This file is part of minos framework.
#
# Minos framework can not be copied and/or distributed without the express
# permission of Clariteia SL.
import functools

from aiohttp import (
    web,
)

from ..configuration import (
    MinosConfig,
)
from ..importlib import (
    import_module,
)


class RestRoutesLoader:
    """
    Rest Interface Handler

    Rest Interface for aiohttp web handling.

    """

    __slots__ = "_endpoints", "_app", "_config"

    def __init__(self, endpoints: dict, config: MinosConfig, app: web.Application = web.Application()):
        self._endpoints = endpoints
        self._app = app
        self._config = config
        self.load_routes()

    def load_routes(self):
        """Load routes from config file."""
        for item in self._endpoints:
            callable_f = self.resolve_callable(item.controller, item.action)
            self._app.router.add_route(item.method, item.route, callable_f)

    def resolve_callable(self, controller: str, action: str):
        """Load controller class and action method.
        :param controller: Controller string. Example: "tests.service.CommandTestService.CommandService"
        :param action: Config instance. Example: "get_order"
        :return: A class method callable instance.
        """
        object_class = import_module(controller)
        instance_class = object_class()
        class_method = getattr(instance_class, action)
        partial = functools.partial(class_method, config=self._config)

        return partial

    def get_app(self):
        """Return rest application instance.
        :return: A `web.Application` instance.
        """
        return self._app
