def get_difficulty_level():
    """Gets the desired difficulty level from the player."""

    while True:
        difficulty = input("Choose a difficulty level (easy, medium, hard): ").lower()
        if difficulty in ["easy", "medium", "hard"]:
            return difficulty
        else:
            print("Invalid difficulty level. Please choose from easy, medium, or hard.")

def display_message(message):
    """Displays a message to the user."""

    print(message)

def get_user_guess():
    """Gets the user's guess."""

    while True:
        try:
            guess = input("Enter your guess: ")
            if not guess:
                raise ValueError("Please enter a number.")
            guess = int(guess)
            return guess
        except ValueError as e:
            print(f"Invalid input: {e}")