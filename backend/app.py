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

    # Initialize the game with the chosen difficulty 
    # if it hasn't been started yet
    if not game.difficulty:
        game.start_game(difficulty)  # Use the start_game method

    # Use the handle_guess method of the Game object
    result = game.handle_guess(guess)
    remaining_guesses = game.get_remaining_guesses()

    return jsonify({'result': result, 'remaining_guesses': remaining_guesses})


@app.route('/reset_game', methods=['POST'])
def reset_game():
    global game  # Access the global game object
    game = Game()  # Reset the game object
    return jsonify({'remaining_guesses': MAX_GUESSES})


if __name__ == '__main__':
    app.run(debug=True)
