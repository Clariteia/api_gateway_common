from aiohttp.test_utils import (
    AioHTTPTestCase,
    unittest_run_loop,
)
import typing as t
from minos.api_gateway.common import (
    MinosConfig,
    RESTService
)
from tests.utils import (
    BASE_PATH,
)
from aiohttp import (
    web,
)


class TestRestService(RESTService):
    def __init__(self, address: str, port: int, endpoints: dict, **kwds: t.Any):
        super().__init__(address=address, port=port, endpoints=endpoints, **kwds)


class TestRestInterfaceService(AioHTTPTestCase):
    CONFIG_FILE_PATH = BASE_PATH / "test_config.yml"

    async def get_application(self):
        """
        Override the get_app method to return your application.
        """
        app = web.Application()
        config = MinosConfig(self.CONFIG_FILE_PATH)
        rest_interface = RESTService(address=config.rest.connection.host,
                                     port=config.rest.connection.port, endpoints=config.rest.endpoints, app=app)

        return await rest_interface.create_application()

    @unittest_run_loop
    async def test_methods(self):
        url = "/order"
        resp = await self.client.request("GET", url)
        assert resp.status == 200
        text = await resp.text()
        assert "Order get" in text

        resp = await self.client.request("POST", url)
        assert resp.status == 200
        text = await resp.text()
        assert "Order added" in text


class TestCustomRestInterfaceService(AioHTTPTestCase):
    CONFIG_FILE_PATH = BASE_PATH / "test_config.yml"

    async def get_application(self):
        """
        Override the get_app method to return your application.
        """
        config = MinosConfig(self.CONFIG_FILE_PATH)
        rest_interface = TestRestService(
            address=config.rest.connection.host, port=config.rest.connection.port, endpoints=config.rest.endpoints)

        return await rest_interface.create_application()

    @unittest_run_loop
    async def test_methods(self):
        url = "/order"
        resp = await self.client.request("GET", url)
        assert resp.status == 200
        text = await resp.text()
        assert "Order get" in text

        resp = await self.client.request("POST", url)
        assert resp.status == 200
        text = await resp.text()
        assert "Order added" in text
