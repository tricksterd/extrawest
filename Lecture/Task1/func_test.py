import unittest
from func import hello_world


class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(hello_world(), 'Hello word!')


if __name__ == "__main__":
    unittest.main()