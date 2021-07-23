import unittest
from lambda_function import Calculator


class Tests(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_calculator_object(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_function_exists(self):
        self.calculator.add

    def test_add_two_numbers(self):
        result = self.calculator.add(10, 2)
        expected = 12

        self.assertEqual(result, expected)

    def test_subtract_function_exists(self):
        self.calculator.subtract

    def test_subtract_two_numbers(self):
        result = self.calculator.subtract(10, 2)
        expected = 8

        self.assertEqual(result, expected)

    def test_divide_function_exists(self):
        self.calculator.divide

    def test_divide_two_numbers(self):
        result = self.calculator.divide(10, 2)
        expected = 5

        self.assertEqual(result, expected)

    def test_multiply_function_exists(self):
        self.calculator.multiply

    def test_multiply_two_numbers(self):
        result = self.calculator.multiply(10, 2)
        expected = 20

        self.assertEqual(result, expected)

if __name__ == "__main__":


    unittest.main()
