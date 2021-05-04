# import library for Python testing
import unittest
from unittest import TestCase

# import library to facilitate testing
import random

# import functions to be tested
from mergesort_recursive import mergesort_recursive, merge_lists


class Test(TestCase):
    def test_list_length_2(self):
        self.assertListEqual(mergesort_recursive([2, 1]), [1, 2])

    def test_list_length_3(self):
        self.assertListEqual(mergesort_recursive([2, 1, 3]), [1, 2, 3])

    def test_random_numbers_length_10(self):
        randomlist = []
        sortedlist = []
        for i in range(10):
            x = random.randint(1, 30)
            randomlist.append(x)
            sortedlist.append(x)
        sortedlist.sort()
        self.assertListEqual(mergesort_recursive(randomlist), sortedlist)

    def test_random_numbers_length_100(self):
        randomlist = []
        sortedlist = []
        for i in range(100):
            x = random.randint(1, 30)
            randomlist.append(x)
            sortedlist.append(x)
        sortedlist.sort()
        self.assertListEqual(mergesort_recursive(randomlist), sortedlist)


if __name__ == '__main__':
    unittest.main()