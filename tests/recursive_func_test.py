import unittest
from recursive_func import factorial


class RecursiveFuncTest(unittest.TestCase):

    def test_recursive_func(self):
        number = 5
        result = factorial(number)
        self.assertEqual(result, 120)
