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