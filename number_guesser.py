import random
from utils import check_guess


def number_guessing_game():
    """Runs the number guessing game."""

    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I've chosen a secret number between 1 and 100.")

    while True:
        try:
            guess = input("Enter your guess: ")
            if not guess:  # Check for empty input
                raise ValueError("Please enter a number.")

            guess = int(guess)  # Convert to integer after checking for empty input
            if guess < 1 or guess > 100:  # Check if guess is outside the range
                raise ValueError("Your guess must be between 1 and 100.")

            attempts += 1

            result = check_guess(guess, secret_number)
            print(result)

            if "Congratulations" in result:
                print(f"You guessed the number in {attempts} attempts.")
                break

        except ValueError as e:
            print(f"Invalid input: {e}")  # Print specific error message


if __name__ == "__main__":
    number_guessing_game()