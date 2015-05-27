from mathquiz import seconds_counter, quiz
import unittest

class TestMathquiz(unittest.TestCase):
    
    def test_seconds_counter(self):
        actual = seconds_counter(55, 3)
        expected = 8
        self.assertEqual(actual, expected)
    
    def test_quiz(self):
        self.assertRaises(TypeError, quiz, "test1", "test2")
        expected = 8
        actual = quiz(3, 5)
        self.assertEqual(expected, actual)
        
if __name__ == "__main__":
    unittest.main()

