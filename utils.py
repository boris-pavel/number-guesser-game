def check_guess(guess, secret_number):
    if guess < secret_number:
        return "Your guess is too low. Try a higher number."
    elif guess > secret_number:
        return "Your guess is too high. Try a lower number."
    else:
        return f"Congratulations! You guessed the number."
    
def get_difficulty_level():
    """Gets the desired difficulty level from the player."""

    while True:
        difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
        if difficulty in ["easy", "medium", "hard"]:
            return difficulty
        else:
            print("Invalid difficulty level. Please choose from easy, medium, or hard.")
