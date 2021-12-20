from unittest import TestCase

from day18 import SnailFishNumber, data_prep, part2


# noinspection DuplicatedCode
class Test(TestCase):
    def test_explode_1(self):
        test_snail_number = SnailFishNumber([[[[[9, 8], 1], 2], 3], 4])
        test_snail_number.explode()
        actual = test_snail_number.get_number()
        expected = [[[[0, 9], 2], 3], 4]
        self.assertEqual(actual, expected)

    def test_explode_2(self):
        test_snail_number = SnailFishNumber([7, [6, [5, [4, [3, 2]]]]])
        test_snail_number.explode()
        actual = test_snail_number.get_number()
        expected = [7, [6, [5, [7, 0]]]]
        self.assertEqual(actual, expected)

    def test_explode_3(self):
        test_snail_number = SnailFishNumber([[6, [5, [4, [3, 2]]]], 1])
        test_snail_number.explode()
        actual = test_snail_number.get_number()
        expected = [[6, [5, [7, 0]]], 3]
        self.assertEqual(actual, expected)

    def test_explode_4(self):
        test_snail_number = SnailFishNumber([[3, [2, [1, [7, 3]]]], [6, [5, [4, [3, 2]]]]])
        test_snail_number.explode()
        actual = test_snail_number.get_number()
        expected = [[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]]
        self.assertEqual(actual, expected)

    def test_explode_5(self):
        test_snail_number = SnailFishNumber([[3, [2, [8, 0]]], [9, [5, [4, [3, 2]]]]])
        test_snail_number.explode()
        actual = test_snail_number.get_number()
        expected = [[3, [2, [8, 0]]], [9, [5, [7, 0]]]]
        self.assertEqual(actual, expected)

    def test_split1(self):
        test_snail_number = SnailFishNumber([[[[0, 7], 4], [15, [0, 13]]], [1, 1]])
        test_snail_number.split()
        actual = test_snail_number.get_number()
        expected = [[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]]
        self.assertEqual(actual, expected)

    def test_split2(self):
        test_snail_number = SnailFishNumber([[[[0, 7], 4], [[7, 8], [0, 13]]], [1, 1]])
        test_snail_number.split()
        actual = test_snail_number.get_number()
        expected = [[[[0, 7], 4], [[7, 8], [0, [6, 7]]]], [1, 1]]
        self.assertEqual(actual, expected)

    def test_reduce(self):
        test_snail_number = SnailFishNumber([[[[[4, 3], 4], 4], [7, [[8, 4], 9]]], [1, 1]])
        test_snail_number.reduce()
        actual = test_snail_number.get_number()
        expected = [[[[0, 7], 4], [[7, 8], [6, 0]]], [8, 1]]
        self.assertEqual(actual, expected)

    def test_addition1(self):
        test_snail_number = SnailFishNumber(
            [[[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]],
             [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]])
        test_snail_number.reduce()
        actual = test_snail_number.get_number()
        expected = [[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]]
        self.assertEqual(actual, expected)

    def test_addition2(self):
        test_snail_number = SnailFishNumber([[[[[4, 0], [5, 4]], [[7, 7], [6, 0]]], [[8, [7, 7]], [[7, 9], [5, 0]]]],
                                             [[2, [[0, 8], [3, 4]]], [[[6, 7], 1], [7, [1, 6]]]]])
        test_snail_number.reduce()
        actual = test_snail_number.get_number()
        expected = [[[[6, 7], [6, 7]], [[7, 7], [0, 7]]], [[[8, 7], [7, 7]], [[8, 8], [8, 0]]]]
        self.assertEqual(actual, expected)

    def test_addition3(self):
        test_snail_number = SnailFishNumber(
            [[[[[6, 7], [6, 7]], [[7, 7], [0, 7]]], [[[8, 7], [7, 7]], [[8, 8], [8, 0]]]],
             [[[[2, 4], 7], [6, [0, 5]]], [[[6, 8], [2, 8]], [[2, 1], [4, 5]]]]])
        test_snail_number.reduce()
        actual = test_snail_number.get_number()
        expected = [[[[7, 0], [7, 7]], [[7, 7], [7, 8]]], [[[7, 7], [8, 8]], [[7, 7], [8, 7]]]]
        self.assertEqual(actual, expected)

    def test_addition4(self):
        test_snail_number = SnailFishNumber(
            [[[[[7, 7], [7, 8]], [[9, 5], [8, 7]]], [[[6, 8], [0, 8]], [[9, 9], [9, 0]]]],
             [[2, [2, 2]], [8, [8, 1]]]])
        test_snail_number.reduce()
        actual = test_snail_number.get_number()
        expected = [[[[6, 6], [6, 6]], [[6, 0], [6, 7]]], [[[7, 7], [8, 9]], [8, [8, 1]]]]
        self.assertEqual(actual, expected)

    def test_addition5(self):
        test_snail_number = SnailFishNumber(
            [[[[[6, 6], [6, 6]], [[6, 0], [6, 7]]], [[[7, 7], [8, 9]], [8, [8, 1]]]],
             [2, 9]])
        test_snail_number.reduce()
        actual = test_snail_number.get_number()
        expected = [[[[6, 6], [7, 7]], [[0, 7], [7, 7]]], [[[5, 5], [5, 6]], 9]]
        self.assertEqual(actual, expected)

    def test_addition6(self):
        test_snail_number = SnailFishNumber(
            [[[[[6, 6], [6, 6]], [[6, 0], [6, 7]]], [[[7, 7], [8, 9]], [8, [8, 1]]]],
             [2, 9]])
        test_snail_number.reduce()
        actual = test_snail_number.get_number()
        expected = [[[[6, 6], [7, 7]], [[0, 7], [7, 7]]], [[[5, 5], [5, 6]], 9]]
        self.assertEqual(actual, expected)

    def test_addition7(self):
        test_snail_number = SnailFishNumber([[[[[6, 6], [7, 7]], [[0, 7], [7, 7]]], [[[5, 5], [5, 6]], 9]],
                                             [1, [[[9, 3], 9], [[9, 0], [0, 7]]]]])
        test_snail_number.reduce()
        actual = test_snail_number.get_number()
        expected = [[[[7, 8], [6, 7]], [[6, 8], [0, 8]]], [[[7, 7], [5, 0]], [[5, 5], [5, 6]]]]
        self.assertEqual(actual, expected)

    def test_addition8(self):
        test_snail_number = SnailFishNumber(
            [[[[[7, 8], [6, 7]], [[6, 8], [0, 8]]], [[[7, 7], [5, 0]], [[5, 5], [5, 6]]]],
             [[[5, [7, 4]], 7], 1]])
        test_snail_number.reduce()
        actual = test_snail_number.get_number()
        expected = [[[[7, 7], [7, 7]], [[8, 7], [8, 7]]], [[[7, 0], [7, 7]], 9]]
        self.assertEqual(actual, expected)

    def test_addition9(self):
        test_snail_number = SnailFishNumber(
            [[[[[7, 7], [7, 7]], [[8, 7], [8, 7]]], [[[7, 0], [7, 7]], 9]],
             [[[[4, 2], 2], 6], [8, 7]]])
        test_snail_number.reduce()
        actual = test_snail_number.get_number()
        expected = [[[[8, 7], [7, 7]], [[8, 6], [7, 7]]], [[[0, 7], [6, 6]], [8, 7]]]
        self.assertEqual(actual, expected)

    def test_magnitude(self):
        test_snail_number = SnailFishNumber([[1, 2], [[3, 4], 5]])
        actual = test_snail_number.get_magnitude()
        expected = 143
        self.assertEqual(actual, expected)

    def test_part2(self):
        day = '18_test'
        test_input_data = data_prep(day)

        actual = part2(test_input_data)
        expected = 3993
        self.assertEqual(actual, expected)
