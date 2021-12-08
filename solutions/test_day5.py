from unittest import TestCase

from day5 import data_prep, part1, part2


# noinspection DuplicatedCode
class Test(TestCase):

    def test_part1(self):
        day = '5_test'
        test_lines = data_prep(day)
        test_grid_size = [max(test_lines[:, i]) for i in range(4)]
        test_grid_size = [max(test_grid_size[0], test_grid_size[2]) + 1,
                          max(test_grid_size[1], test_grid_size[3]) + 1]
        actual = part1(test_lines, test_grid_size)
        expected = 5
        self.assertEqual(actual, expected)

    def test_part2(self):
        day = '5_test'
        test_lines = data_prep(day)
        test_grid_size = [max(test_lines[:, i]) for i in range(4)]
        test_grid_size = [max(test_grid_size[0], test_grid_size[2]) + 1,
                          max(test_grid_size[1], test_grid_size[3]) + 1]
        actual = part2(test_lines, test_grid_size)
        expected = 12
        self.assertEqual(actual, expected)
