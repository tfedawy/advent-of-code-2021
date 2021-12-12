from unittest import TestCase

from day12 import data_prep, part1, part2


class Test(TestCase):
    def test_part1_1(self):
        day = '12_test1'
        test_adjacency_data = data_prep(day)
        actual = part1(test_adjacency_data)
        expected = 10
        self.assertEqual(actual, expected)

    def test_part1_2(self):
        day = '12_test2'
        test_adjacency_data = data_prep(day)
        actual = part1(test_adjacency_data)
        expected = 19
        self.assertEqual(actual, expected)

    def test_part1_3(self):
        day = '12_test3'
        test_adjacency_data = data_prep(day)
        actual = part1(test_adjacency_data)
        expected = 226
        self.assertEqual(actual, expected)

    def test_part2_1(self):
        day = '12_test1'
        test_adjacency_data = data_prep(day)
        actual = part2(test_adjacency_data)
        expected = 36
        self.assertEqual(actual, expected)

    def test_part2_2(self):
        day = '12_test2'
        test_adjacency_data = data_prep(day)
        actual = part2(test_adjacency_data)
        expected = 103
        self.assertEqual(actual, expected)

    def test_part2_3(self):
        day = '12_test3'
        test_adjacency_data = data_prep(day)
        actual = part2(test_adjacency_data)
        expected = 3509
        self.assertEqual(actual, expected)

    def test_part1_paths_and_count1(self):
        day = '12_test1'
        test_adjacency_data = data_prep(day)
        actual = part1(test_adjacency_data, 'paths and count')
        expected = 10
        self.assertEqual(actual, expected)

    def test_part1_paths_and_count2(self):
        day = '12_test2'
        test_adjacency_data = data_prep(day)
        actual = part1(test_adjacency_data, 'paths and count')
        expected = 19
        self.assertEqual(actual, expected)

    def test_part1_paths_and_count3(self):
        day = '12_test3'
        test_adjacency_data = data_prep(day)
        actual = part1(test_adjacency_data, 'paths and count')
        expected = 226
        self.assertEqual(actual, expected)

    def test_part2_paths_and_count1(self):
        day = '12_test1'
        test_adjacency_data = data_prep(day)
        actual = part2(test_adjacency_data, 'paths and count')
        expected = 36
        self.assertEqual(actual, expected)

    def test_part2_paths_and_count2(self):
        day = '12_test2'
        test_adjacency_data = data_prep(day)
        actual = part2(test_adjacency_data, 'paths and count')
        expected = 103
        self.assertEqual(actual, expected)

    def test_part2_paths_and_count3(self):
        day = '12_test3'
        test_adjacency_data = data_prep(day)
        actual = part2(test_adjacency_data, 'paths and count')
        expected = 3509
        self.assertEqual(actual, expected)
