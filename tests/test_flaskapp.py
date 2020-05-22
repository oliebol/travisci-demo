import unittest

from main import *

class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_multiply(self):
        # given
        x = 10
        y = 12

        # when
        answer = multiply(x, y)

        # then
        self.assertEqual(answer, 120)

    def test_hello_happy(self):
        result = hello()
        self.assertEqual(result, "Hello World!")

    def test_uppercase_happy(self):
        s = "Lorem ipsum dolor sit amet"
        result = touppercase(s)
        self.assertEqual(result, "LOREM IPSUM DOLOR SIT AMET")

    def test_uppercase_sad(self):
        s = 12
        with self.assertRaises(AttributeError):
            result = touppercase(s)

    def test_hello_sad(self):
        with self.assertRaises(TypeError):
            result = hello(1234)

    def test_hello_expect_fail(self):
        result = hello()
        self.assertEqual(result, "Farewell world! :(")


if __name__ == '__main__':
    unittest.main()