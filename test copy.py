""" basic test for GitHub CI process"""
import unittest
from lambda_function import basic_function


class TestStringMethod(unittest.TestCase):
    """ basic test"""

    def test_basic_function_fails(self):
        """ fail test"""
        self.assertNotEqual(basic_function(), ".")

    def test_basic_function_pass(self):
        """ pass test"""
        self.assertEqual(basic_function(), "hello world")


if __name__ == '__main__':
    unittest.main()
