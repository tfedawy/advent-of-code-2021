from unittest import TestCase

from day8 import data_prep, part1, part2, part2_pattern_matching


class Test(TestCase):
    def test_part1(self):
        day = '8_test'
        test_signal = data_prep(day)
        known_numbers = {2: 1, 3: 7, 4: 4, 7: 8}
        actual = part1(test_signal, known_numbers)
        expected = 26
        self.assertEqual(actual, expected)

    def test_part2(self):
        day = '8_test'
        test_signal = data_prep(day)
        actual = part2(test_signal)
        expected = 61229
        self.assertEqual(actual, expected)

    def test_part2_pattern_matching(self):
        day = '8_test'
        test_signal = data_prep(day)
        known_numbers = {2: 1, 3: 7, 4: 4, 7: 8}
        actual = part2_pattern_matching(test_signal, known_numbers)
        expected = 61229
        self.assertEqual(actual, expected)
