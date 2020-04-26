import unittest
from cycle import cycle


class TestCycle(unittest.TestCase):
    def test_with_more_elements_than_in_the_list_repeats(self):
        elements = [1, 2, 3]
        cyclic_list = cycle(elements)
        result = []

        for i in range(4):
            result.append(next(cyclic_list))

        self.assertEqual([1, 2, 3, 1], result)


if __name__ == '__main__':
    unittest.main()
