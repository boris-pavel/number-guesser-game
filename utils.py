def check_guess(guess, secret_number):
    if guess < secret_number:
        return "Your guess is too low. Try a higher number."
    elif guess > secret_number:
        return "Your guess is too high. Try a lower number."
    else:
        return f"Congratulations! You guessed the number."