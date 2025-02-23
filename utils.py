from constants import *

def check_guess(guess, secret_number):
    """Checks the player's guess against the secret number."""

    if guess < secret_number:
        return TOO_LOW_MESSAGE
    elif guess > secret_number:
        return TOO_HIGH_MESSAGE
    else:
        return CORRECT_GUESS_MESSAGE

def get_number_range(difficulty):
    """Returns the minimum and maximum numbers for the given difficulty level."""

    if difficulty == "easy":
        return 1, 10
    elif difficulty == "medium":
        return 1, 50
    else:  # difficulty == "hard"
        return 1, 100