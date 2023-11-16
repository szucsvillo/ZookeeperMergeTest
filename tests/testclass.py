# tests/testclass.py

import unittest

class TestClass(unittest.TestCase):

    def test_nothing(self):

        # Assert
        self.assertEqual(5, 5, "Testing nothing")

if __name__ == '__main__':
    unittest.main()
