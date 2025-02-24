const guessInput = document.getElementById('guess');
const submitButton = document.getElementById('submit');
const difficultySelect = document.getElementById('difficulty');
const messageDiv = document.getElementById('message');
const remainingGuessesDiv = document.getElementById('remaining-guesses');

submitButton.addEventListener('click', () => {
  const guess = parseInt(guessInput.value);
  const difficulty = difficultySelect.value;

  // Validate input
  if (isNaN(guess)) {
    messageDiv.textContent = "Please enter a valid number.";
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
    messageDiv.textContent = `Please enter a number between ${minNum} and ${maxNum}.`;
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
    messageDiv.textContent = data.result;
    remainingGuessesDiv.textContent = `Remaining Guesses: ${data.remaining_guesses}`;

    if (data.result === "Congratulations! You guessed the number." || data.remaining_guesses === 0) {
      // End the game
      guessInput.disabled = true;
      submitButton.disabled = true;
      difficultySelect.disabled = true;
    }
  })
  .catch(error => {
    console.error('Error:', error);
    messageDiv.textContent = "An error occurred.";
  });
});