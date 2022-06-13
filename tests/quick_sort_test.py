import unittest
from quick_sort import quick_sort


class QuickSortTest(unittest.TestCase):

    def test_quick_sort(self):
        numbers = [2, 5, 7, 8, 10, 15, 1, 3]
        result = quick_sort(numbers)
        self.assertEqual(result, [1, 2, 3, 5, 7, 8, 10, 15])
