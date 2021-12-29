from unittest import TestCase

from day22 import data_prep, part1, part2


class Test(TestCase):
    def test_part1(self):
        day = '22_test_1'
        test_instructions, test_projections, test_cuboids = data_prep(day)

        actual = part1(test_instructions, test_projections)
        expected = 590784
        self.assertEqual(actual, expected)

    def test_part2(self):
        day = '22_test_2'
        test_instructions, test_projections, test_cuboids = data_prep(day)

        actual = part2(test_instructions, test_cuboids)
        expected = 2758514936282235
        self.assertEqual(actual, expected)
