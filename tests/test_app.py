import unittest
from app import main

class TestApp(unittest.TestCase):
    def test_main(self):
        self.assertEqual(main(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
