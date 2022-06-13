from selection_sort import find_smallest, selection_sort
import unittest


class SelectionSortTest(unittest.TestCase):

    def test_find_smallest(self):
        items = [6, 8, 4, 1, 10]
        result = find_smallest(items)
        self.assertEqual(result, 3)

    def test_selection_sort(self):
        items = [6, 8, 4, 1, 10]
        result = selection_sort(items)
        self.assertEqual(result, [1, 4, 6, 8, 10])
