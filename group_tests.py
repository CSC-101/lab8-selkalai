import unittest
import group


class MyTestCase(unittest.TestCase):
    def test_groups_of_3_1(self):
        input = [1, 2, 3, 4]
        actual = group.groups_of_3(input)
        expected = [[1, 2, 3], [4]]
        self.assertEqual(actual, expected)

    def test_groups_of_3_2(self):
        input = [1, 2, 3, 4, 5, 6]
        actual = group.groups_of_3(input)
        expected = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(actual, expected)

    def test_groups_of_3_3(self):
        input = []
        actual = group.groups_of_3(input)
        expected = []
        self.assertEqual(actual, expected)

    def test_groups_of_3_4(self):
        input = [1]
        actual = group.groups_of_3(input)
        expected = [[1]]
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
