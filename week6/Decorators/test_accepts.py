import unittest
from accepts import accepts


class TestAccepts(unittest.TestCase):
    def test_with_zero_arguments(self):
        @accepts()
        def print_correct():
            return "Correct"

        result = print_correct()

        self.assertEqual("Correct", result)

    def test_with_one_argument(self):
        @accepts(str)
        def say_hello(name):
            return "Hello, I am {}".format(name)

        result = say_hello("Tanya")

        self.assertEqual("Hello, I am Tanya", result)

    def test_with_one_wrong_argument_raises_error(self):
        @accepts(str)
        def say_hello(name):
            return "Hello, I am {}".format(name)

        with self.assertRaises(TypeError):
            say_hello(4)

    def test_with_wrong_number_of_arguments_raises_error(self):
        @accepts(str)
        def say_hello(name):
            return "Hello, I am {}".format(name)

        with self.assertRaises(TypeError):
            say_hello(4, "pop")

        with self.assertRaises(TypeError):
            say_hello()

    def test_with_more_arguments(self):
        @accepts(str, int)
        def deposit(name, money):
            return "{} sends {} $!".format(name, money)

        result = deposit("Marto", 10)

        self.assertEqual("Marto sends 10 $!", result)


if __name__ == '__main__':
    unittest.main()
