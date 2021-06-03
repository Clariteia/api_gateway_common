"""
Copyright (C) 2021 Clariteia SL

This file is part of minos framework.

Minos framework can not be copied and/or distributed without the express permission of Clariteia SL.
"""
from typing import (
    Any,
)

import aiohttp

from .abc import (
    ClientHttpBase,
)

HTTP_GET = "GET"
HTTP_DELETE = "DELETE"
HTTP_OPTIONS = "OPTIONS"
HTTP_PATCH = "PATCH"
HTTP_POST = "POST"
HTTP_PUT = "PUT"


class ClientHttp(ClientHttpBase):
    """HTTP Client aiohttp."""

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    async def get(self, url: str, params: dict = None, **kwargs: Any):
        """GET method.
        :param url: Url to call.
        :param params: Params to send on URL.
        :param kwargs: Additional named arguments.
        :return: A `_RequestContextManager` instance.
        """
        return await self._trigger_request(HTTP_GET, url, params, **kwargs)

    async def post(self, url: str, params: dict = None, data: Any = None, **kwargs: Any):
        """POST method.
        :param url: Url to call.
        :param params: Params to send on URL.
        :param data: Data to send in body.
        :param kwargs: Additional named arguments.
        :return: A `_RequestContextManager` instance.
        """
        return await self._trigger_request(HTTP_POST, url, params, data, **kwargs)

    async def put(self, url: str, params: dict = None, data: Any = None, **kwargs: Any):
        """PUT method.
        :param url: Url to call.
        :param params: Params to send on URL.
        :param data: Data to send in body.
        :param kwargs: Additional named arguments.
        :return: A `_RequestContextManager` instance.
        """
        return await self._trigger_request(HTTP_PUT, url, params, data, **kwargs)

    async def patch(self, url: str, params: dict = None, data: Any = None, **kwargs: Any):
        """PATCH method.
        :param url: Url to call.
        :param params: Params to send on URL.
        :param data: Data to send in body.
        :param kwargs: Additional named arguments.
        :return: A `_RequestContextManager` instance.
        """
        return await self._trigger_request(HTTP_PATCH, url, params, data, **kwargs)

    async def delete(self, url: str, params: dict = None, data: Any = None, **kwargs: Any):
        """POST method.
        :param url: Url to call.
        :param params: Params to send on URL.
        :param data: Data to send in body.
        :param kwargs: Additional named arguments.
        :return: A `_RequestContextManager` instance.
        """
        return await self._trigger_request(HTTP_DELETE, url, params, data, **kwargs)

    async def _trigger_request(self, method: str, url: str, params, data: Any = None, **kwargs: Any):
        """Trigger the request.
        :param method: HTTP method.
        :param url: Url to call.
        :param params: Params to send on URL.
        :param data: Data to send in body.
        :param kwargs: Additional named arguments.
        :return: A `_RequestContextManager` instance.
        """
        return await self.session.request(method=method, url=url, params=params, data=data, **kwargs)
