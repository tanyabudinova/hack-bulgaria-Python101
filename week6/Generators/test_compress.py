import unittest
from compress import compress


class TestCompress(unittest.TestCase):
    def test_if_all_masks_are_false_returns_empty_list(self):
        compressed = list(compress(["Ivo", "Rado", "Panda"], [False, False, False]))

        self.assertEqual([], compressed)

    def test_if_returns_list_with_all_masked(self):
        compressed = list(compress(["Ivo", "Rado", "Panda"], [False, False, True]))

        self.assertTrue("Panda" in compressed)

    def test_if_returns_list_with_only_masked_elements(self):
        compressed = list(compress(["Ivo", "Rado", "Panda"], [False, False, True]))

        self.assertEqual(["Panda"], compressed)


if __name__ == '__main__':
    unittest.main()
