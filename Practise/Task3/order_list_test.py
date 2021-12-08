import unittest
from order_list import test_data


class TestHelloWorld(unittest.TestCase):

    def test_result_data(self):
        result = [
            'Lucky Numbers',
            'Sports',
            'Live Sports',
            'Betgames',
            'Pragmatic Play Games'
        ]
        self.assertEqual(test_data(), result)


if __name__ == "__main__":
    unittest.main()
