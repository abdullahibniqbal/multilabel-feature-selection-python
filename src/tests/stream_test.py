import unittest

from src.multilabel.streams.stream import Stream


class StreamTest(unittest.TestCase):
    def test_map(self):
        expected = [2, 3, 4, 5]
        actual = Stream([1, 2, 3, 4]).map(lambda elem: elem+1).as_list()

        assert expected == actual, "should be [2, 3, 4, 5]"

    def test_filter(self):
        expected = [2, 4]
        actual = Stream([1, 2, 3, 4]).filter(lambda elem: elem%2 == 0).as_list()

        assert expected == actual, "should be all even numbers"

    def test_chaining(self):
        expected = [3, 5]
        actual =                            \
            Stream([1, 2, 3, 4])            \
        .filter(lambda elem: elem%2 == 0)   \
        .map(lambda elem: elem+1)           \
        .as_list()                          \

        assert expected == actual, "should be [3, 5]"

    def test_append_list(self):
        expected = [1, 2, 3, 4, 5, 6]
        actual =                        \
            Stream([1, 2])              \
            .append_list([3, 4])        \
            .append_list([5, 6])        \
            .as_list()

        print("actual: ", actual)

        assert expected == actual, "should be [1, 2, 3, 4, 5, 6]"

    def test_append_elem(self):
        expected = [1, 2, 3, 4]
        actual =                \
            Stream([1, 2])      \
            .append_elem(3)     \
            .append_elem(4)     \
            .as_list()

        print("actual: ", actual)

        assert expected == actual, "should be [1, 2, 3, 4]"


if __name__ == '__main__':
    unittest.main()
