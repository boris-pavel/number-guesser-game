import random
from io_handler import display_message, get_user_guess
from constants import (
    MAX_GUESSES, WELCOME_MESSAGE, SECRET_NUMBER_RANGE_MESSAGE,
    GUESSES_LEFT_MESSAGE, GUESS_RANGE, CORRECT_GUESS_MESSAGE,
    ATTEMPS_TRIED, OUT_OF_GUESSES_MESSAGE, SECRET_NUMBER_WAS_MESSAGE,
    TOO_LOW_MESSAGE, TOO_HIGH_MESSAGE
)


class Difficulty:
    """
    Represents the difficulty level of the game.
    """
    def __init__(self, name, min_num, max_num):
        """
        Initializes the difficulty level with a name,
        minimum, and maximum numbers.
        """
        self.name = name
        self.min_num = min_num
        self.max_num = max_num


class Game:
    """
    Represents a number guessing game.
    """
    def __init__(self):
        """
        Initializes the game with the difficulty level,
        secret number, remaining guesses, and game status.
        """
        self.difficulty = None
        self.secret_number = None
        self.remaining_guesses = None
        self.game_won = False

    def start_game(self):
        """
        Starts the game by setting the difficulty level,
        generating a secret number, and prompting the user for guesses.
        """
        self.set_difficulty()
        self.secret_number = random.randint(
            self.difficulty.min_num,
            self.difficulty.max_num
            )
        self.remaining_guesses = MAX_GUESSES
        self.game_won = False

        display_message(WELCOME_MESSAGE)
        display_message(
            SECRET_NUMBER_RANGE_MESSAGE.format(self.difficulty.min_num,
                                               self.difficulty.max_num))
        display_message(GUESSES_LEFT_MESSAGE.format(self.remaining_guesses))

        while self.remaining_guesses > 0 and not self.game_won:
            self.handle_guess()

    def set_difficulty(self, difficulty):
        """
        Sets the difficulty level of the game.
        """
        if difficulty == "easy":
            self.difficulty = Difficulty("easy", 1, 10)
        elif difficulty == "medium":
            self.difficulty = Difficulty("medium", 1, 50)
        else:
            self.difficulty = Difficulty("hard", 1, 100)

    def handle_guess(self):
        """
        Handles the user's guess by checking if it is correct,
        too low, or too high.
        """
        guess = get_user_guess()
        if guess < self.difficulty.min_num or guess > self.difficulty.max_num:
            display_message(
                GUESS_RANGE.format(
                    self.difficulty.min_num,
                    self.difficulty.max_num
                    ))
            return

        self.remaining_guesses -= 1
        result = self.check_guess(guess)
        display_message(result)

        if CORRECT_GUESS_MESSAGE in result:
            display_message(
                ATTEMPS_TRIED.format(MAX_GUESSES - self.remaining_guesses))
            self.game_won = True
        elif self.remaining_guesses > 0:
            display_message(GUESSES_LEFT_MESSAGE.format(
                self.remaining_guesses))
        else:
            display_message(OUT_OF_GUESSES_MESSAGE)
            display_message(SECRET_NUMBER_WAS_MESSAGE.format(
                self.secret_number))

    def check_guess(self, guess):
        """
        Checks the user's guess against the secret number.
        """
        if guess < self.secret_number:
            return TOO_LOW_MESSAGE
        elif guess > self.secret_number:
            return TOO_HIGH_MESSAGE
        else:
            return CORRECT_GUESS_MESSAGE

    def get_secret_number(self):
        """Returns the secret number."""
        return self.secret_number

    def get_remaining_guesses(self):
        """Returns the remaining guesses."""
        return self.remaining_guesses
