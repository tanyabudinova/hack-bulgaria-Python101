import unittest
from utils import parse_length

class TestParseLength(unittest.TestCase):
    def test_length_with_hours(self):
        length = "3:24:34"

        result = parse_length(length)

        self.assertEqual((3,24,34), result)

    def test_length_with_miutes_over_an_hour_without_hours(self):
        length = "123:45"

        result = parse_length(length)

        self.assertEqual((2,3,45), result)

    def test_length_with_miutes_over_an_hour_with_hours_raises_error(self):
        length = "3:123:45"

        exc = None

        try:
            parse_length(length)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),"Incorrect minutes!")

    def test_length_with_seconds_over_a_minute_raises_error(self):
        length = "14:65"

        exc = None

        try:
            parse_length(length)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),"Incorrect seconds!")

    def test_correct_length(self):
        length_only_seconds = "54"
        length_minutes = "15:54"
        length_hours = "8:15:54"

        result = parse_length(length_only_seconds)
        result2 = parse_length(length_minutes)
        result3 = parse_length(length_hours)

        self.assertEqual((0,0,54),result)
        self.assertEqual((0,15,54),result2)
        self.assertEqual((8,15,54),result3)



if __name__ == '__main__':
    unittest.main()