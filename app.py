import random
from flask import Flask, request, jsonify
from number_guesser import Game, MAX_GUESSES
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
game = Game()


@app.route('/check_guess', methods=['POST'])
def check_guess():
    global game  # Access the global game object

    data = request.get_json()
    guess = data['guess']
    difficulty = data['difficulty']

    # Initialize the game with the chosen
    # difficulty if it hasn't been started yet
    if not game.difficulty:
        game.set_difficulty(difficulty)  # Set the difficulty directly
        game.secret_number = random.randint(
            game.difficulty.min_num,
            game.difficulty.max_num
            )
        game.remaining_guesses = MAX_GUESSES

    # Use the check_guess method of the Game object
    result = game.check_guess(guess)
    remaining_guesses = game.get_remaining_guesses()

    return jsonify({'result': result, 'remaining_guesses': remaining_guesses})


if __name__ == '__main__':
    app.run(debug=True)
