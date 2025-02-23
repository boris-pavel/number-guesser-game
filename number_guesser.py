import random
from io_handler import get_difficulty_level, display_message, get_user_guess
from constants import (
    MAX_GUESSES, WELCOME_MESSAGE, SECRET_NUMBER_RANGE_MESSAGE,
    GUESSES_LEFT_MESSAGE, GUESS_RANGE, CORRECT_GUESS_MESSAGE,
    ATTEMPS_TRIED, OUT_OF_GUESSES_MESSAGE, SECRET_NUMBER_WAS_MESSAGE,
    TOO_LOW_MESSAGE, TOO_HIGH_MESSAGE
)


class Difficulty:
    def __init__(self, name, min_num, max_num):
        self.name = name
        self.min_num = min_num
        self.max_num = max_num


class Game:
    """
    Represents the number guessing game.

    Attributes:
        difficulty (Difficulty): The difficulty level of the game.
        secret_number (int): The secret number to be guessed.
        remaining_guesses (int): The number of guesses the player has left.
        game_won (bool): Indicates whether the game has been won.
    """
    def __init__(self):
        """Initializes the game with default values."""
        self.difficulty = None
        self.secret_number = None
        self.remaining_guesses = None
        self.game_won = False

    def start_game(self):
        """Starts the number guessing game."""
        self.set_difficulty()
        self.secret_number = random.randint(
            self.difficulty.min_num, self.difficulty.max_num
            )
        self.remaining_guesses = MAX_GUESSES

        display_message(WELCOME_MESSAGE)
        display_message(
            SECRET_NUMBER_RANGE_MESSAGE.format(
                self.difficulty.min_num, self.difficulty.max_num
                )
            )
        display_message(GUESSES_LEFT_MESSAGE.format(self.remaining_guesses))

        while self.remaining_guesses > 0 and not self.game_won:
            self.handle_guess()

    def set_difficulty(self):
        """Sets the difficulty level of the game."""
        difficulty_name = get_difficulty_level()
        if difficulty_name == "easy":
            self.difficulty = Difficulty("easy", 1, 10)
        elif difficulty_name == "medium":
            self.difficulty = Difficulty("medium", 1, 50)
        else:
            self.difficulty = Difficulty("hard", 1, 100)

    def handle_guess(self):
        """Handles a single guess from the player."""
        guess = get_user_guess()
        if guess < self.difficulty.min_num or guess > self.difficulty.max_num:
            display_message(
                GUESS_RANGE.format(
                    self.difficulty.min_num, self.difficulty.max_num
                    )
            )
            return

        self.remaining_guesses -= 1
        result = self.check_guess(guess)
        display_message(result)

        if CORRECT_GUESS_MESSAGE in result:
            display_message(
                ATTEMPS_TRIED.format(MAX_GUESSES - self.remaining_guesses)
                )
            self.game_won = True
        elif self.remaining_guesses > 0:
            display_message(
                GUESSES_LEFT_MESSAGE.format(self.remaining_guesses)
                )
        else:
            display_message(OUT_OF_GUESSES_MESSAGE)
            display_message(SECRET_NUMBER_WAS_MESSAGE.format(
                self.secret_number
                ))

    def check_guess(self, guess):
        """Checks the player's guess against the secret number."""
        if guess < self.secret_number:
            return TOO_LOW_MESSAGE
        elif guess > self.secret_number:
            return TOO_HIGH_MESSAGE
        else:
            return CORRECT_GUESS_MESSAGE


if __name__ == "__main__":
    game = Game()
    game.start_game()
