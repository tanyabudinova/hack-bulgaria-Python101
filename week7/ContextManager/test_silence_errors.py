import unittest
from silence_errors import silence, silence_func


class TestSilence(unittest.TestCase):
    def test_silences_the_correct_exception(self):
        exc = None

        try:
            with silence(ValueError):
                raise ValueError()
        except Exception as err:
            exc = err

        self.assertIsNone(exc)

    def test_does_not_silence_the_other_exceptions(self):
        exc = None

        try:
            with silence(ValueError):
                raise TypeError()
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)

    def test_silences_the_correct_exception_with_the_correct_message(self):
        exc = None

        try:
            with silence(ValueError, "Test"):
                raise ValueError("Test")
        except Exception as err:
            exc = err

        self.assertIsNone(exc)

    def test_silences_the_correct_exception_with_the_wrong_message(self):
        exc = None

        try:
            with silence(ValueError, "Testing."):
                raise ValueError("Test")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)


class TestSilenceFunction(unittest.TestCase):
    def test_function_silences_the_correct_exception(self):
        exc = None

        try:
            with silence_func(ValueError):
                raise ValueError()
        except Exception as err:
            exc = err

        self.assertIsNone(exc)

    def test_does_not_silence_function_the_other_exceptions(self):
        exc = None

        try:
            with silence_func(ValueError):
                raise TypeError()
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)

    def test_function_silences_the_correct_exception_with_the_correct_message(self):
        exc = None

        try:
            with silence_func(ValueError, "Test"):
                raise ValueError("Test")
        except Exception as err:
            exc = err

        self.assertIsNone(exc)

    def test_function_silences_the_correct_exception_with_the_wrong_message(self):
        exc = None

        try:
            with silence_func(ValueError, "Testing."):
                raise ValueError("Test")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)


if __name__ == '__main__':
    unittest.main()
