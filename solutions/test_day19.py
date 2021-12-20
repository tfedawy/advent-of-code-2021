from unittest import TestCase

from day19 import data_prep, part1, part2


class Test(TestCase):
    def test_part1(self):
        day = '19_test'
        test_scanners = data_prep(day)

        actual, _ = part1(test_scanners)
        expected = 79
        self.assertEqual(actual, expected)

    def test_part2(self):
        day = '19_test'
        test_scanners = data_prep(day)
        part1(test_scanners)

        actual = part2(test_scanners)
        expected = 3621
        self.assertEqual(actual, expected)
