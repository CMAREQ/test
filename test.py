import unittest
from cosa import birthdayCakeCandles

class TestCake(unittest.TestCase):

    def testCandles(self):
        self.assertEqual(birthdayCakeCandles(4, [2, 2, 2, 2]), 4)

if __name__ == '__main__':
    unittest.main()
