import unittest
from main import *


class TestTask2(unittest.TestCase):

    def test_findMaxInt(self):
        self.assertIsNone(findMaxInt())

    def test_findMinInt(self):
        self.assertIsNone(findMinInt())

    def test_floatWithMoney(self):
        self.assertEqual(floatWithMoney(), 0.3)

    def test_decimalWithMoney(self):
        self.assertEqual(decimalWithMoney(), Decimal("0.3"))

    def test_maxString(self):
        self.assertIsNone(maxString())


if __name__ == "__main__":
    unittest.main()
