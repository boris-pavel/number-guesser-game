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
            guess = int(input("Enter your guess: "))
            attempts += 1

            result = check_guess(guess, secret_number)
            print(result)

            if "Congratulations" in result:  # Check for the congratulatory message
                print(f"You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    number_guessing_game()