import unittest
from decimal_precision import *


class TestChangePrecision(unittest.TestCase):
    def test_printing_to_the_correct_digit(self):
        with change_precision(2):
            num = (decimal.Decimal('1.11') + decimal.Decimal('2.111'))

            self.assertEqual(decimal.Decimal('3.2'), num)

    def test_correct_rounding(self):
        with change_precision(2):
            num = (decimal.Decimal('1.12') + decimal.Decimal('2.131'))

            self.assertEqual(decimal.Decimal('3.3'), num)

    def test_if_affects_outside_the_manager(self):
        with change_precision(2):
            num = (decimal.Decimal('1.11') + decimal.Decimal('2.111'))

            self.assertEqual(decimal.Decimal('3.2'), num)
        num = (decimal.Decimal('1.11') + decimal.Decimal('2.111'))
        self.assertEqual(decimal.Decimal('3.2'), num)


if __name__ == '__main__':
    unittest.main()
