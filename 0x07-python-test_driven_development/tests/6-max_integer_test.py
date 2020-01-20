import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertAlmostEqual(max_integer([1, 10, 25, 7]), 25)
        self.assertAlmostEqual(max_integer([1]), 1)
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer(), None)
        self.assertAlmostEqual(max_integer(["hello", "python", "error", "eeeeeee"]), "eeeeeee")
        self.assertAlmostEqual(max_integer([-1, -2, -3, 0]), 0)
        self.assertAlmostEqual(max_integer([9, 2, 3, 4]), 9)
