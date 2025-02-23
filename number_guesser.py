import random
from utils import check_guess, get_number_range  # Import get_number_range
from io_handler import get_difficulty_level, display_message, get_user_guess
from constants import (
    WELCOME_MESSAGE,
    SECRET_NUMBER_RANGE_MESSAGE,
    GUESSES_LEFT_MESSAGE,
    GUESS_RANGE,
    ATTEMPTS_TRIED,
    OUT_OF_GUESSES_MESSAGE,
    SECRET_NUMBER_WAS_MESSAGE
)


MAX_GUESSES = 7  # Define the maximum number of guesses allowed


def number_guessing_game():
    """
    Runs the number guessing game with difficulty levels and a limited number
    of guesses.
    """

    difficulty = get_difficulty_level()
    min_num, max_num = get_number_range(difficulty)

    secret_number = random.randint(min_num, max_num)
    remaining_guesses = MAX_GUESSES  # Initialize remaining guesses

    display_message(WELCOME_MESSAGE)  # Use WELCOME_MESSAGE constant
    display_message(SECRET_NUMBER_RANGE_MESSAGE.format(min_num, max_num))

    display_message(GUESSES_LEFT_MESSAGE.format(remaining_guesses))

    while remaining_guesses > 0:
        guess = get_user_guess()
        if guess < min_num or guess > max_num:
            display_message(GUESS_RANGE.format(min_num, max_num))
            continue

        remaining_guesses -= 1  # Decrement remaining guesses

        result = check_guess(guess, secret_number)
        display_message(result)

        if "Congratulations" in result:
            attempts = MAX_GUESSES - remaining_guesses
            display_message(ATTEMPTS_TRIED.format(attempts))
            break
        else:
            if remaining_guesses > 0:
                display_message(GUESSES_LEFT_MESSAGE.format(remaining_guesses))
            else:
                display_message(OUT_OF_GUESSES_MESSAGE)
                display_message(
                    SECRET_NUMBER_WAS_MESSAGE.format(secret_number)
                )


if __name__ == "__main__":
    number_guessing_game()
