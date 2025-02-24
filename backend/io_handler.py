from constants import (
    DIFFICULTY_PROMPT,
    EMPTY_INPUT_MESSAGE,
    INVALID_DIFFICULTY_MESSAGE,
    GUESS_PROMPT,
    INVALID_INPUT_MESSAGE
)  # Import necessary constants


def get_difficulty_level() -> str:
    """Gets the difficulty level from the user."""
    while True:
        difficulty = input(DIFFICULTY_PROMPT).lower()
        if difficulty in ['easy', 'medium', 'hard']:
            return difficulty
        else:
            print(INVALID_DIFFICULTY_MESSAGE)


def display_message(message: str) -> None:
    """Displays a message to the user."""
    print(message)


def get_user_guess() -> int:
    """Gets the user's guess."""
    while True:
        try:
            guess = input(GUESS_PROMPT)
            if not guess:
                raise ValueError(EMPTY_INPUT_MESSAGE)
            guess = int(guess)
            return guess
        except ValueError as e:
            print(INVALID_INPUT_MESSAGE.format(e))
