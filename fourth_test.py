import unittest
import fourth

class TestExtend(unittest.TestCase):

    def test_given_argument_is_int(self):
        self.assertRaises(TypeError, fourth.greeter, 123)

    def test_given_argument_is_list(self):
        self.assertRaises(TypeError, fourth.greeter, ['alma', 1, 45])

    def test_given_argument_is_name(self):
        self.assertEqual(fourth.greeter('Peter'), 'Hello, Peter!')

if __name__ == '__main__':
    unittest.main()
