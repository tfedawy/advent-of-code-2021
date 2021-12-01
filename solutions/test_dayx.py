from unittest import TestCase

from day1 import data_prep, part1, part2


class Test(TestCase):
    def test_part1(self):
        day = 'x_test'
        test_data = data_prep(day)

        actual = part1()
        expected = 0
        self.assertEqual(actual, expected)

    def test_part2(self):
        day = 'x_test'
        test_data = data_prep(day)

        actual = part2()
        expected = 0
        self.assertEqual(actual, expected)