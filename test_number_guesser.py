import unittest
from unittest import mock
import unittest
from utils import check_guess
from io_handler import get_difficulty_level  # Import from io_handler.py

class TestNumberGuesser(unittest.TestCase):

    def test_guess_is_too_low(self):
        result = check_guess(20, 50)
        self.assertEqual(result, "Your guess is too low. Try a higher number.")

    def test_guess_is_too_high(self):
        result = check_guess(70, 50)
        self.assertEqual(result, "Your guess is too high. Try a lower number.")

    def test_guess_is_correct(self):
        result = check_guess(50, 50)
        self.assertEqual(result, "Congratulations! You guessed the number.")

    def test_get_difficulty_level_valid_input(self):
        # We can't directly test input(), so we'll simulate it
        # by mocking the input function.
        with unittest.mock.patch('builtins.input', return_value='medium'):
            difficulty = get_difficulty_level()
            self.assertEqual(difficulty, 'medium')

    def test_get_difficulty_level_invalid_input(self):
         with unittest.mock.patch('builtins.input', side_effect=['blah', 'easy']):
            difficulty = get_difficulty_level()
            self.assertEqual(difficulty, 'easy')

if __name__ == "__main__":
    unittest.main()