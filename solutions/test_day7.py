from unittest import TestCase

from day7 import part1, part2


class Test(TestCase):
    def test_part1(self):
        test_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        actual = part1(test_input)
        expected = 37
        self.assertEqual(actual, expected)

    def test_part2(self):
        test_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        actual = part2(test_input)
        expected = 168
        self.assertEqual(actual, expected)
