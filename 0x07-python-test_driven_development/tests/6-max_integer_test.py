#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_last(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    
    def test_max_one_elem(self):
        self.assertEqual(max_integer([44]), 44)

    def test_max_mid(self):
        self.assertEqual(max_integer([1, 9]), 9)

    def test_max_one_negative(self):
        self.assertEqual(max_integer([-321, 0, 53, 40]), 53)

    def test_max_all_negative(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)


    def test_max_empty_list(self):
        self.assertEqual(max_integer([]), None)

if __name__ == '__main__':
    unittest.main()
