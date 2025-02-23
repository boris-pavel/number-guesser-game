import random
from utils import check_guess
from io_handler import get_difficulty_level, display_message, get_user_guess

MAX_GUESSES = 7  # Define the maximum number of guesses allowed

def number_guessing_game():
    """
    Runs the number guessing game with difficulty levels and a limited number of guesses.
    """

    difficulty = get_difficulty_level()

    if difficulty == "easy":
        min_num, max_num = 1, 10
    elif difficulty == "medium":
        min_num, max_num = 1, 50
    else:  # difficulty == "hard"
        min_num, max_num = 1, 100

    secret_number = random.randint(min_num, max_num)
    remaining_guesses = MAX_GUESSES  # Initialize remaining guesses

    display_message("Welcome to the Number Guessing Game!")
    display_message(f"I've chosen a secret number between {min_num} and {max_num}.")
    display_message(f"You have {remaining_guesses} guesses.")  # Display initial guesses

    while remaining_guesses > 0:
        guess = get_user_guess()
        if guess < min_num or guess > max_num:
            display_message(f"Your guess must be between {min_num} and {max_num}.")
            continue

        remaining_guesses -= 1  # Decrement remaining guesses

        result = check_guess(guess, secret_number)
        display_message(result)

        if "Congratulations" in result:
            display_message(f"You guessed the number in {MAX_GUESSES - remaining_guesses} attempts.")
            break
        else:
            if remaining_guesses > 0:
                display_message(f"You have {remaining_guesses} guesses left.")
            else:
                display_message("You're out of guesses! Game over.")
                display_message(f"The secret number was {secret_number}.")

if __name__ == "__main__":
    number_guessing_game()