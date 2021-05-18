"""
Copyright (C) 2021 Clariteia SL

This file is part of minos framework.

Minos framework can not be copied and/or distributed without the express permission of Clariteia SL.
"""
import unittest

from minos.api_gateway.common import classname
from minos.api_gateway.common import import_module
from minos.api_gateway.common import MinosImportException


class TestImportlib(unittest.TestCase):
    def test_import_module(self):
        object_class = import_module("tests.ImportedModule.ImportedClassTest")
        self.assertEqual("tests.ImportedModule.ImportedClassTest", classname(object_class))

    def test_not_callable_module(self):
        with self.assertRaises(TypeError) as context:
            import_module("tests.ImportedModule.notcallble")

            self.assertTrue("The module is not callable" in context.exception)

    def test_import_module_exception(self):
        with self.assertRaises(MinosImportException):
            import_module("tests.ImportedModuleFail.ImportedClassTest")

    def test_classname(self):
        self.assertEqual("builtins.int", classname(int))
        self.assertEqual(
            "minos.api_gateway.common.exceptions.MinosImportException", classname(MinosImportException),
        )


if __name__ == "__main__":
    unittest.main()
