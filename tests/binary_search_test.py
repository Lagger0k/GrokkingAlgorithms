from binary_search import binary_search
import unittest


class BinarySearchTest(unittest.TestCase):

    def test_binary_search(self):
        my_list = [1, 3, 4, 5, 7, 9]
        result = binary_search(my_list, 5)
        self.assertEqual(result, 3)

    def test_binary_search_out_of_list(self):
        my_list = [1, 3, 4, 5, 7, 9]
        result = binary_search(my_list, 10)
        self.assertEqual(result, None)
