from unittest import TestCase

from day25 import data_prep, SeaFloor, part1


class Test(TestCase):
    def test_part1(self):
        day = '25_test'
        test_grid = data_prep(day)
        test_sea_floor = SeaFloor(test_grid)

        actual = part1(test_sea_floor)
        expected = 58
        self.assertEqual(actual, expected)
