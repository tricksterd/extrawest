import unittest
from main import *


class TestTask2(unittest.TestCase):

    def test_find_max_int(self):
        self.assertIsNone(find_max_int())

    def test_find_min_int(self):
        self.assertIsNone(find_min_int())

    def test_float_with_money(self):
        self.assertEqual(float_with_money(), 0.3)

    def test_decimal_with_money(self):
        self.assertEqual(decimal_with_money(), Decimal("0.3"))

    def test_max_string(self):
        self.assertIsNone(max_string())


if __name__ == "__main__":
    unittest.main()
