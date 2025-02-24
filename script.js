const guessInput = document.getElementById('guess');
const submitButton = document.getElementById('submit');
const difficultySelect = document.getElementById('difficulty');
const messageDiv = document.getElementById('message');

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
  fetch('/check_guess', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ guess: guess, difficulty: difficulty })
  })
.then(response => response.json())
.then(data => {
    // Handle response from backend
    messageDiv.textContent = data.result;

    if (data.result === "Correct!") {
      // TODO: End the game or display a congratulatory message
    } else {
      // TODO: Update remaining guesses and allow another guess
    }
  })
.catch(error => {
    console.error('Error:', error);
    messageDiv.textContent = "An error occurred.";
  });
});