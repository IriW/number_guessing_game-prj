# Number Guessing Game

Welcome to the Number Guessing Game! This project is a simple implementation of a number guessing game using Python.

## How to Play

1. **Start the Game**: Run the script, and you will be greeted with a welcome message.
2. **Choose Difficulty**: You will be prompted to choose a difficulty level: 'easy' or 'hard'.
3. **Make a Guess**: The program will randomly pick a number between 1 and 100. You need to guess the number.
4. **Hints**: After each guess, you will receive a hint whether your guess was too high or too low.
5. **Attempts**: You have a limited number of attempts based on the chosen difficulty level to guess the correct number.

## Game Rules

- In 'easy' mode, you have 10 attempts to guess the number.
- In 'hard' mode, you have 5 attempts to guess the number.
- After each guess, you will be informed if your guess is too high or too low.
- If you guess the correct number within the allowed attempts, you win.
- If you run out of attempts without guessing the correct number, you lose.

## Functions

- `check_answer(guessed_number, computer_number)`: Checks the user's guess against the computer's number and provides feedback.
- `check_difficulty()`: Prompts the user to choose a difficulty level and returns the number of attempts based on the choice.

## Running the Game

To play the game, simply run the script:

```sh
python number_guessing_game.py
```

You will be prompted to start the game and choose a difficulty level. Follow the on-screen instructions to play.

Enjoy the game!
