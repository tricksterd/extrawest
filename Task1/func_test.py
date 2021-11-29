import unittest
from func import helloWorld


class TestHelloWorld(unittest.TestCase):

    def test_HelloWorld(self):
        self.assertEqual(helloWorld(), 'Hello word!')


if __name__ == "__main__":
    unittest.main()