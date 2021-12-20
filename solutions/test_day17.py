from unittest import TestCase

from day17 import data_prep, find_velocities, part1, part2


class Test(TestCase):
    def test_part1(self):
        day = '17_test'
        test_min_x, test_max_x, test_min_y, test_max_y = data_prep(day)
        test_initial_velocity = find_velocities(test_min_x, test_max_x, test_min_y, test_max_y)
        actual = part1(test_initial_velocity)
        expected = 45
        self.assertEqual(actual, expected)

    def test_part2(self):
        day = '17_test'
        test_min_x, test_max_x, test_min_y, test_max_y = data_prep(day)
        test_initial_velocity = find_velocities(test_min_x, test_max_x, test_min_y, test_max_y)
        actual = part2(test_initial_velocity)
        expected = 112
        self.assertEqual(actual, expected)
