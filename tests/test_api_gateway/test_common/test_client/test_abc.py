from unittest import IsolatedAsyncioTestCase

from minos.api_gateway.common import ClientHttp


class TestClient(IsolatedAsyncioTestCase):
    async def test_get(self):
        async with ClientHttp() as client:
            request = await client.get(url="http://httpbin.org/get")
            self.assertEqual(request.status, 200)

            # Test parameters
            params = {"test": 1}

            request = await client.get(url="http://httpbin.org/get", params=params)
            self.assertEqual(request.url.query_string, "test=1")
            result = await request.text()
            self.assertIsNotNone(result)
            self.assertEqual(request.status, 200)

    async def test_post(self):
        async with ClientHttp() as client:
            request = await client.post(url="http://httpbin.org/post")
            self.assertEqual(request.status, 200)
            result = await request.text()
            self.assertIsNotNone(result)

            # Test parameters
            params = {"test": 1}
            request = await client.post(url="http://httpbin.org/post", params=params)
            self.assertEqual(request.url.query_string, "test=1")
            self.assertEqual(request.status, 200)
            result = await request.text()
            self.assertIsNotNone(result)

            # Test data
            data = {"test": "data_test"}
            request = await client.post(url="http://httpbin.org/post", params=params, data=data)
            result = await request.text()
            self.assertIsNotNone(result)
            self.assertEqual(request.status, 200)

    async def test_put(self):
        async with ClientHttp() as client:
            request = await client.put(url="http://httpbin.org/put")
            self.assertEqual(request.status, 200)
            result = await request.text()
            self.assertIsNotNone(result)

            # Test parameters
            params = {"test": 1}
            request = await client.put(url="http://httpbin.org/put", params=params)
            self.assertEqual(request.url.query_string, "test=1")
            self.assertEqual(request.status, 200)
            result = await request.text()
            self.assertIsNotNone(result)

            # Test data
            data = {"test": "data_test"}
            request = await client.put(url="http://httpbin.org/put", params=params, data=data)
            self.assertEqual(request.status, 200)
            result = await request.text()
            self.assertIsNotNone(result)

    async def test_patch(self):
        async with ClientHttp() as client:
            request = await client.patch(url="http://httpbin.org/patch")
            self.assertEqual(request.status, 200)
            result = await request.text()
            self.assertIsNotNone(result)

            # Test parameters
            params = {"test": 1}
            request = await client.patch(url="http://httpbin.org/patch", params=params)
            self.assertEqual(request.url.query_string, "test=1")
            self.assertEqual(request.status, 200)
            result = await request.text()
            self.assertIsNotNone(result)

            # Test data
            data = {"test": "data_test"}
            request = await client.patch(url="http://httpbin.org/patch", params=params, data=data)
            self.assertEqual(request.status, 200)
            result = await request.text()
            self.assertIsNotNone(result)

    async def test_delete(self):
        async with ClientHttp() as client:
            request = await client.delete(url="http://httpbin.org/delete")
            self.assertEqual(request.status, 200)
            result = await request.text()
            self.assertIsNotNone(result)

            # Test parameters
            params = {"test": 1}
            request = await client.delete(url="http://httpbin.org/delete", params=params)
            self.assertEqual(request.url.query_string, "test=1")
            self.assertEqual(request.status, 200)
            result = await request.text()
            self.assertIsNotNone(result)

            # Test data
            data = {"test": "data_test"}
            request = await client.delete(url="http://httpbin.org/delete", params=params, data=data)
            self.assertEqual(request.status, 200)
            result = await request.text()
            self.assertIsNotNone(result)
