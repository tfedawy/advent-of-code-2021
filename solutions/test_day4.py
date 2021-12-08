from unittest import TestCase

from day4 import data_prep, play, part1, part2


class Test(TestCase):

    def test_part1(self):
        day = '4_test'
        test_guess, test_boards = data_prep(day)
        test_winners = play(test_guess, test_boards)
        actual = part1(test_winners)
        expected = 4512
        self.assertEqual(actual, expected)

    def test_part2(self):
        day = '4_test'
        test_guess, test_boards = data_prep(day)
        test_winners = play(test_guess, test_boards)
        actual = part2(test_winners)
        expected = 1924
        self.assertEqual(actual, expected)
