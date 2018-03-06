import unittest
import functions

class TestFunctions(unittest.TestCase):
    def setup(self):
        pass

    def test_increment_one(self):
        self.assertEqual(functions.increment_one(0),1)


    def test_increment_two(self):
        self.assertEqual(functions.increment_two(0),2)

if __name__ == '__main__':
    unittest.main()
