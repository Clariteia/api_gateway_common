from unittest import IsolatedAsyncioTestCase

from aiohttp import web

from minos.api_gateway.common import MinosConfig
from minos.api_gateway.common import RestRoutesLoader
from tests.utils import BASE_PATH


class TestRestInterfaceLoader(IsolatedAsyncioTestCase):
    async def test_load_endpoints(self):
        conf = MinosConfig(path=BASE_PATH / "test_config.yml")
        app = web.Application()
        rest = RestRoutesLoader(endpoints=conf.rest.endpoints, app=app)
        app = rest.get_app()
        self.assertIsInstance(app, web.Application)
