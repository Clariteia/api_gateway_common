# Copyright (C) 2020 Clariteia SL
#
# This file is part of minos framework.
#
# Minos framework can not be copied and/or distributed without the express
# permission of Clariteia SL.
import typing as t

from aiohttp import (
    web,
)
from aiomisc.service.aiohttp import (
    AIOHTTPService,
)

from ..configuration import (
    MinosConfig,
)
from .loader import (
    RestRoutesLoader,
)


class RESTService(AIOHTTPService):
    """
    Rest Interface

    Expose REST Interface handler using aiomisc AIOHTTPService.

    """

    def __init__(
        self,
        address: str,
        port: int,
        endpoints: dict,
        config: MinosConfig,
        app: web.Application = web.Application(),
        **kwds: t.Any
    ):
        address = address
        port = port
        super().__init__(address=address, port=port, **kwds)
        self._endpoints = endpoints
        self.rest_interface = RestRoutesLoader(endpoints=endpoints, config=config, app=app)

    async def create_application(self):
        return self.rest_interface.get_app()  # pragma: no cover
