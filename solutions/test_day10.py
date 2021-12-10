from unittest import TestCase

from day10 import data_prep, lines_parser, part1, part2


class Test(TestCase):
    def test_part1(self):
        day = '10_test'
        test_lines = data_prep(day)
        test_corrupting_characters, _ = lines_parser(test_lines)
        actual = part1(test_corrupting_characters)
        expected = 26397
        self.assertEqual(actual, expected)

    def test_part2(self):
        day = '10_test'
        test_lines = data_prep(day)
        _, test_completion_lists = lines_parser(test_lines)
        actual = part2(test_completion_lists)
        expected = 288957
        self.assertEqual(actual, expected)
