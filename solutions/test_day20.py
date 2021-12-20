from unittest import TestCase

from day20 import data_prep, Image, part1, part2


class Test(TestCase):
    def test_part1(self):
        day = '20_test'
        test_img, test_enhancement_algorithm = data_prep(day)
        test_image = Image(test_img, test_enhancement_algorithm)

        actual = part1(test_image, 2)
        expected = 35
        self.assertEqual(actual, expected)

    def test_part2(self):
        day = '20_test'
        test_img, test_enhancement_algorithm = data_prep(day)
        test_image = Image(test_img, test_enhancement_algorithm)

        actual = part2(test_image, 50)
        expected = 3351
        self.assertEqual(actual, expected)
