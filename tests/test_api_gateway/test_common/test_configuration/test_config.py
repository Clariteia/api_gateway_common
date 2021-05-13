"""
Copyright (C) 2021 Clariteia SL

This file is part of minos framework.

Minos framework can not be copied and/or distributed without the express permission of Clariteia SL.
"""
import os
import unittest
from unittest import (
    mock,
)

from minos.api_gateway.common import (
    MinosConfig,
    MinosConfigAbstract,
    MinosConfigDefaultAlreadySetException,
    MinosConfigException,
)
from tests.utils import (
    BASE_PATH,
)


class TestMinosConfig(unittest.TestCase):
    def setUp(self) -> None:
        self.config_file_path = BASE_PATH / "test_config.yml"

    def test_config_ini_fail(self):
        with self.assertRaises(MinosConfigException):
            MinosConfig(path=BASE_PATH / "test_fail_config.yaml")

    def test_config_rest(self):
        config = MinosConfig(path=self.config_file_path)
        rest = config.rest

        broker = rest.connection
        self.assertEqual("localhost", broker.host)
        self.assertEqual(8900, broker.port)

        endpoints = rest.endpoints
        self.assertEqual("AddOrder", endpoints[0].name)

    @mock.patch.dict(os.environ, {"API_GATEWAY_REST_HOST": "::1"})
    def test_overwrite_with_environment(self):
        config = MinosConfig(path=self.config_file_path)
        rest = config.rest
        self.assertEqual("::1", rest.connection.host)

    @mock.patch.dict(os.environ, {"API_GATEWAY_REST_HOST": "::1"})
    def test_overwrite_with_environment_false(self):
        config = MinosConfig(path=self.config_file_path, with_environment=False)
        rest = config.rest
        self.assertEqual("localhost", rest.connection.host)

    def test_get_default_default(self):
        with MinosConfig(path=self.config_file_path) as config:
            self.assertEqual(config, MinosConfigAbstract.get_default())

    def test_multiple_default_config_raises(self):
        with self.assertRaises(MinosConfigDefaultAlreadySetException):
            with MinosConfig(path=self.config_file_path):
                with MinosConfig(path=self.config_file_path):
                    pass


if __name__ == "__main__":
    unittest.main()
