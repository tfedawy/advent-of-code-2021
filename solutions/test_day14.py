from unittest import TestCase

from day14 import data_prep, part1, part2


class Test(TestCase):
    def test_part1(self):
        day = '14_test'
        test_polymer_template, test_pair_insertion = data_prep(day)
        actual = part1(test_polymer_template, test_pair_insertion, 10)
        expected = 1588
        self.assertEqual(actual, expected)

    def test_part2(self):
        day = '14_test'
        test_polymer_template, test_pair_insertion = data_prep(day)
        actual = part2(test_polymer_template, test_pair_insertion, 40)
        expected = 2188189693529
        self.assertEqual(actual, expected)
