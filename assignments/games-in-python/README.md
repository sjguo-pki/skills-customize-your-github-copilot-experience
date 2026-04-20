
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python to practice strings, loops, conditionals, and user input. By the end of this assignment, you will create a complete game loop with clear win and lose outcomes.

## 📝 Tasks

### 🛠️ Build the Core Hangman Loop

#### Description
Create the main game flow for Hangman. Your program should choose a random word, repeatedly ask the player to guess letters, and update the game state after each guess.

#### Requirements
Completed program should:

- Select a random word from a predefined list.
- Show current progress using placeholders for unknown letters (for example: `_ _ _ _`).
- Accept one letter guess at a time from the player.
- Continue looping until the player either guesses the full word or runs out of attempts.

### 🛠️ Track Guesses and End the Game

#### Description
Add logic that handles correct and incorrect guesses, tracks remaining attempts, and displays final game messages.

#### Requirements
Completed program should:

- Decrease remaining attempts only when the player guesses an incorrect letter.
- Prevent repeated guesses from being counted as new incorrect attempts.
- Display a clear win message when the word is fully guessed.
- Display a clear lose message that reveals the correct word when attempts reach zero.
