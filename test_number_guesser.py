import unittest
from unittest.mock import patch
from utils import check_guess
from io_handler import get_user_guess, get_difficulty_level
from number_guesser import Game, Difficulty


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

    @patch('number_guesser.get_difficulty_level', return_value='easy')
    def test_set_difficulty_easy(self, mock_get_difficulty_level):
        game = Game()
        game.set_difficulty()
        self.assertEqual(game.difficulty.name, 'easy')
        self.assertEqual(game.difficulty.min_num, 1)
        self.assertEqual(game.difficulty.max_num, 10)

    @patch('number_guesser.get_user_guess', return_value=5)
    def test_handle_guess_valid_guess(self, mock_get_user_guess):
        game = Game()
        game.difficulty = Difficulty('easy', 1, 10)
        game.secret_number = 5
        game.remaining_guesses = 3
        game.handle_guess()
        self.assertEqual(game.remaining_guesses, 2)
        self.assertTrue(game.game_won)

    @patch('number_guesser.get_user_guess', return_value=15)
    def test_handle_guess_out_of_range_guess(self, mock_get_user_guess):
        game = Game()
        game.difficulty = Difficulty('easy', 1, 10)
        game.secret_number = 5
        game.remaining_guesses = 3
        game.handle_guess()
        self.assertEqual(game.remaining_guesses, 3)
        self.assertFalse(game.game_won)


if __name__ == "__main__":
    unittest.main()
