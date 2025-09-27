# Python Mini Projects

This repository contains a collection of Python projects. The purpose of this repository is to keep practice projects organized in one place and to document progress as I continue learning and experimenting with Python. Each project is stored in its own folder and contains a `main.py` file along with a workspace.

## Purpose

* Build a strong foundation in Python through hands-on coding.
* Explore different problem-solving approaches.
* Maintain an organized record of practice projects in one place.

## How to Use

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```
2. Navigate into a project folder:

   ```bash
   cd project-folder-name
   ```
3. Run the project:

   ```bash
   python main.py
   ```

Each project folder is independent and can be run on its own.

---

## Projects

### Word Guessing Game

A terminal-based word guessing game where the player attempts to guess a randomly chosen word one letter at a time.

* A word is randomly selected from a predefined word bank.
* The player has 10 attempts to guess the word correctly.
* Correct guesses reveal the letter’s position(s) in the word.
* Incorrect guesses reduce the remaining attempts.
* The game ends when the player either guesses the full word or runs out of attempts.

**Usage:**

```bash
python main.py
```

**Example Gameplay:**

```
Current word: _ _ _ _ _ _

Guess the letter: o
Oop! Wrong Guess, Attempts left: 9

Current word: _ _ _ _ _ _

Guess the letter: y
Wow! You guessed right!

Current word: _ y _ _ _ _
```

---

### Roman Numeral Converter

Converts Roman numerals into integers based on user input.

* Handles basic numerals (`I`, `V`, `X`, `L`, `C`, `D`, `M`).
* Supports multi-character inputs such as `XX`, `XII`, or `MCM`.
* Usage:

  ```bash
  python main.py
  ```

  Example input/output:

  ```
  Enter the roman numeral: XX
  Entered roman numeral translates to: 20
  ```

---
