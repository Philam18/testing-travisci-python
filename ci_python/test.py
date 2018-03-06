import unittest
import functions

class TestFunctions(unittest.TestCase):
    def setup(self):
        pass

    def test_increment_one(self):
        self.assertEqual(functions.increment_one(4),10)


    def test_increment_two(self):
        self.assertEqual(functions.increment_two(4),8)

if __name__ == '__main__':
    unittest.main()
