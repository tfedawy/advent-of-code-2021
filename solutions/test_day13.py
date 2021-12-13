from unittest import TestCase

from day13 import data_prep, TransparentPaper, part1


class Test(TestCase):
    def test_part1(self):
        day = '13_test'
        test_dots, test_instructions = data_prep(day)
        test_paper = TransparentPaper(test_dots)
        actual = part1(test_paper, test_instructions[0])
        expected = 17
        self.assertEqual(actual, expected)
