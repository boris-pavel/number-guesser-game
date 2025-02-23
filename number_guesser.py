import random

def check_guess(guess, secret_number):
    """Checks the player's guess against the secret number.

    Args:
        guess: The player's guess (integer).
        secret_number: The secret number (integer).

    Returns:
        A string indicating the result of the guess ("Too low!", "Too high!", or a congratulatory message).
    """
    if guess < secret_number:
        return "Too low!"
    elif guess > secret_number:
        return "Too high!"
    else:
        return f"Congratulations! You guessed the number."


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