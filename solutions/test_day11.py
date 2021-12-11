from unittest import TestCase

from day11 import data_prep, OctopusGrid, part1, part2


class Test(TestCase):
    def test_part1_10(self):
        day = '11_test'
        test_octopus_data = data_prep(day)
        test_octopus_grid = OctopusGrid(test_octopus_data)
        actual = part1(test_octopus_grid, 10)
        expected = 204
        self.assertEqual(actual, expected)

    def test_part1_100(self):
        day = '11_test'
        test_octopus_data = data_prep(day)
        test_octopus_grid = OctopusGrid(test_octopus_data)
        actual = part1(test_octopus_grid, 100)
        expected = 1656
        self.assertEqual(actual, expected)

    def test_part2(self):
        day = '11_test'
        test_octopus_data = data_prep(day)
        test_octopus_grid = OctopusGrid(test_octopus_data)
        actual = part2(test_octopus_grid)
        expected = 195
        self.assertEqual(actual, expected)
