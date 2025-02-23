import random
from utils import check_guess, get_difficulty_level  # Import necessary functions

def number_guessing_game():
    """Runs the number guessing game with difficulty levels."""

    difficulty = get_difficulty_level()  # Get difficulty level from utils.py

    if difficulty == "easy":
        min_num, max_num = 1, 10
    elif difficulty == "medium":
        min_num, max_num = 1, 50
    else:  # difficulty == "hard"
        min_num, max_num = 1, 100

    secret_number = random.randint(min_num, max_num)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print(f"I've chosen a secret number between {min_num} and {max_num}.")

    while True:
        try:
            guess = input("Enter your guess: ")
            if not guess:  # Check for empty input
                raise ValueError("Please enter a number.")

            guess = int(guess)  # Convert to integer after checking for empty input
            if guess < min_num or guess > max_num:  # Check if guess is outside the range
                raise ValueError(f"Your guess must be between {min_num} and {max_num}.")

            attempts += 1

            result = check_guess(guess, secret_number)  # Use check_guess from utils.py
            print(result)

            if "Congratulations" in result:
                print(f"You guessed the number in {attempts} attempts.")
                break

        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
    number_guessing_game()