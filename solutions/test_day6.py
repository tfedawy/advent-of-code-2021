from unittest import TestCase

from day6 import fish_growth


class Test(TestCase):
    def test_18(self):
        test_input = [3, 4, 3, 1, 2]
        actual = fish_growth(test_input, 18)
        expected = 26
        self.assertEqual(actual, expected)

    def test_80(self):
        test_input = [3, 4, 3, 1, 2]
        actual = fish_growth(test_input, 80)
        expected = 5934
        self.assertEqual(actual, expected)

    def test_256(self):
        test_input = [3, 4, 3, 1, 2]
        actual = fish_growth(test_input, 256)
        expected = 26984457539
        self.assertEqual(actual, expected)
