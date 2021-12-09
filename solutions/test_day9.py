from unittest import TestCase

from day9 import data_prep, construct_height_map, find_all_basins_BFS, find_all_basins_recursive, part1, part2


class Test(TestCase):
    def test_part1(self):
        day = '9_test'
        test_signal = data_prep(day)
        test_height_map = construct_height_map(test_signal)
        actual = part1(test_height_map)
        expected = 15
        self.assertEqual(actual, expected)

    def test_part2_bfs(self):
        day = '9_test'
        test_signal = data_prep(day)
        test_height_map = construct_height_map(test_signal)
        test_basins = find_all_basins_BFS(test_height_map)
        actual = part2(test_basins)
        expected = 1134
        self.assertEqual(actual, expected)

    def test_part2_recursive(self):
        day = '9_test'
        test_signal = data_prep(day)
        test_height_map = construct_height_map(test_signal)
        test_basins = find_all_basins_recursive(test_height_map)
        actual = part2(test_basins)
        expected = 1134
        self.assertEqual(actual, expected)
