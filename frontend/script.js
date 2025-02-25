const guessInput = document.getElementById('guess');
const submitButton = document.getElementById('submit');
const difficultySelect = document.getElementById('difficulty');
const congratulationsMessageDiv = document.getElementById('congratulations-message');
const attemptsMessageDiv = document.getElementById('attempts-message');
const resetButton = document.getElementById('reset');

submitButton.addEventListener('click', () => {
  const guess = parseInt(guessInput.value);
  const difficulty = difficultySelect.value;

  // Validate input
  if (isNaN(guess)) {
    congratulationsMessageDiv.textContent = "Please enter a valid number.";
    return;
  }

  let minNum, maxNum;
  if (difficulty === 'easy') {
    minNum = 1;
    maxNum = 10;
  } else if (difficulty === 'medium') {
    minNum = 1;
    maxNum = 50;
  } else {
    minNum = 1;
    maxNum = 100;
  }

  if (guess < minNum || guess > maxNum) {
    congratulationsMessageDiv.textContent = `Please enter a number between ${minNum} and ${maxNum}.`;
    return;
  }

  // Send request to backend
  fetch('http://127.0.0.1:5000/check_guess', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ guess: guess, difficulty: difficulty })
  })
  .then(response => response.json())
  .then(data => {
    if (data.result.includes("Congratulations!")) {
      congratulationsMessageDiv.textContent = "Congratulations!";
      attemptsMessageDiv.textContent = data.result.split("Congratulations!")[1].trim();
    } else {
      congratulationsMessageDiv.textContent = data.result;
      attemptsMessageDiv.textContent = "";
    }

    if (data.result === "Congratulations!" || data.remaining_guesses === 0) {
      // End the game
      guessInput.disabled = true;
      submitButton.disabled = true;
      difficultySelect.disabled = true;
    }
  })
  .catch(error => {
    console.error('Error:', error);
    congratulationsMessageDiv.textContent = "An error occurred.";
  });
});

resetButton.addEventListener('click', () => {
  fetch('http://127.0.0.1:5000/reset_game', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    }
  })
  .then(response => response.json())
  .then(data => {
    // Reset the game state
    guessInput.disabled = false;
    submitButton.disabled = false;
    difficultySelect.disabled = false;
    guessInput.value = '';
    congratulationsMessageDiv.textContent = '';
    attemptsMessageDiv.textContent = '';
  })
  .catch(error => {
    console.error('Error:', error);
    congratulationsMessageDiv.textContent = "An error occurred.";
  });
});

function updateGameMessage() {
    const difficulty = document.getElementById('difficulty').value;
    const gameMessage = document.getElementById('game-message');
    switch (difficulty) {
        case 'easy':
            gameMessage.textContent = "I've chosen a number between 1 and 10.";
            break;
        case 'medium':
            gameMessage.textContent = "I've chosen a number between 1 and 50.";
            break;
        case 'hard':
            gameMessage.textContent = "I've chosen a number between 1 and 100.";
            break;
    }
}
