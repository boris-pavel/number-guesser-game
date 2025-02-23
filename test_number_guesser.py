import unittest
from unittest.mock import patch
from utils import check_guess
from io_handler import get_user_guess, get_difficulty_level


class TestNumberGuesser(unittest.TestCase):
    def test_guess_is_too_low(self) -> None:
        result = check_guess(20, 50)
        self.assertEqual(result, "Your guess is too low. Try a higher number.")

    def test_guess_is_too_high(self) -> None:
        result = check_guess(70, 50)
        self.assertEqual(result, "Your guess is too high. Try a lower number.")

    def test_guess_is_correct(self) -> None:
        result = check_guess(50, 50)
        self.assertEqual(result, "Congratulations! You guessed the number.")

    def test_get_difficulty_level_valid_input(self) -> None:
        # We can't directly test input(), so we'll simulate it
        # by mocking the input function.
        with unittest.mock.patch('builtins.input', return_value='medium'):
            difficulty = get_difficulty_level()
            self.assertEqual(difficulty, 'medium')

    def test_get_difficulty_level_invalid_input(self) -> None:
        with unittest.mock.patch(
                'builtins.input', side_effect=['blah', 'easy']):
            difficulty = get_difficulty_level()
            self.assertEqual(difficulty, 'easy')

    @patch('io_handler.input', return_value='50')
    def test_get_user_guess_valid_input(self, mock_input) -> None:
        guess = get_user_guess()
        self.assertEqual(guess, 50)

    @patch('io_handler.input', side_effect=['invalid', '50'])
    def test_get_user_guess_invalid_input_then_valid(self, mock_input) -> None:
        guess = get_user_guess()
        self.assertEqual(guess, 50)

    @patch('io_handler.input', side_effect=['', '50'])
    def test_get_user_guess_empty_input_then_valid(self, mock_input) -> None:
        guess = get_user_guess()
        self.assertEqual(guess, 50)


if __name__ == "__main__":
    unittest.main()
