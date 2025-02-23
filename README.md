# Number Guessing Game

This is a simple number guessing game written in Python. The computer generates a random number, and the player has to guess it. The game provides feedback on whether the guess is too high or too low and keeps track of the number of attempts.  It also features different difficulty levels.

## How to Play

1.  **Set up the environment:**
    *   It's highly recommended to create a virtual environment to manage your project's dependencies. Open a terminal or command prompt and navigate to your project's directory. Then, create a virtual environment (venv):
        ```bash
        python3 -m venv .venv  # Create a virtual environment
        source .venv/bin/activate  # Activate the virtual environment (Linux/macOS)
        .venv\Scripts\activate  # Activate the virtual environment (Windows)
        ```
    *   Install the `mock` library, which is used for testing:
        ```bash
        pip install mock
        ```
2.  **Run the game:**
    *   Save the Python code as `number_guesser.py` and `utils.py`.
    *   Run the game using the command: `python number_guesser.py`
    *   Follow the on-screen instructions to play the game.
3.  **Run the tests:**
    *   Save the test code as `test_number_guesser.py`.
    *   Run the tests using the command: `python -m unittest test_number_guesser.py`

## Features

*   Random number generation.
*   User input and validation.
*   Feedback on guesses (too high or too low).
*   Tracking of attempts.
*   Difficulty levels (easy, medium, hard).

## Future Enhancements (Optional)

*   Limited guesses.
*   High score tracking.


## Author

Boris-Andrei Pavel


