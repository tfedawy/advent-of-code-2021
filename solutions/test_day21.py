from unittest import TestCase

from day21 import data_prep, part1, part2


class Test(TestCase):
    def test_part1(self):
        day = '21_test'
        test_player1_starting_pos, test_player2_starting_pos = data_prep(day)

        actual = part1(test_player1_starting_pos, test_player2_starting_pos, 1000)
        expected = 739785
        self.assertEqual(actual, expected)

    def test_part2(self):
        day = '21_test'
        test_player1_starting_pos, test_player2_starting_pos = data_prep(day)

        actual = part2(test_player1_starting_pos, test_player2_starting_pos, 21, 3).number_of_wins
        expected = 444356092776315
        self.assertEqual(actual, expected)
