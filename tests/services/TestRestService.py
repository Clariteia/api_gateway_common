from aiohttp import web

from minos.api_gateway.common import MinosConfig


class RestService(object):
    async def add_order(self, request: web.Request, config: MinosConfig, **kwargs):
        return web.Response(text="Order added")

    async def get_order(self, request: web.Request, config: MinosConfig, **kwargs):
        return web.Response(text="Order get")
