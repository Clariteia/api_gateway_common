# Copyright (C) 2020 Clariteia SL
#
# This file is part of minos framework.
#
# Minos framework can not be copied and/or distributed without the express
# permission of Clariteia SL.
from aiohttp import (
    web,
)

from ..importlib import (
    import_module,
)


class RestRoutesLoader:
    """
    Rest Interface Handler

    Rest Interface for aiohttp web handling.

    """

    __slots__ = "_endpoints", "_app"

    def __init__(self, endpoints: dict, app: web.Application = web.Application()):
        self._endpoints = endpoints
        self._app = app
        self.load_routes()

    def load_routes(self):
        """Load routes from config file."""
        for item in self._endpoints:
            callable_f = self.class_resolver(item.controller, item.action)
            self._app.router.add_route(item.method, item.route, callable_f)

    @staticmethod
    def class_resolver(controller: str, action: str):
        """Load controller class and action method.
        :param controller: Controller string. Example: "tests.service.CommandTestService.CommandService"
        :param action: Config instance. Example: "get_order"
        :return: A class method callable instance.
        """
        object_class = import_module(controller)
        instance_class = object_class()
        class_method = getattr(instance_class, action)

        return class_method

    def get_app(self):
        """Return rest application instance.
        :return: A `web.Application` instance.
        """
        return self._app
