from unittest import TestCase

import numpy as np

from day15 import Graph, data_prep, get_data, part1, part2


class Test(TestCase):
    def test_part1(self):
        day = '15_test'
        test_grid = data_prep(day)
        test_graph = Graph(test_grid)
        source = (0, 0)
        actual = part1(test_graph, source)
        expected = 40
        self.assertEqual(actual, expected)

    def test_expand_graph(self):
        day = '15_test'
        test_grid = data_prep(day)
        test_graph = Graph(test_grid)
        expected = test_graph.expand(5)

        actual_day = '15_test2'
        actual = get_data(actual_day)
        actual = actual.split('\n')
        actual = np.array([list(map(int, list(i))) for i in actual])

        self.assertFalse((actual - expected).any())

    def test_part2(self):
        day = '15_test'
        test_grid = data_prep(day)
        test_graph = Graph(test_grid)
        source = (0, 0)
        actual = part2(test_graph, source)
        expected = 315
        self.assertEqual(actual, expected)
