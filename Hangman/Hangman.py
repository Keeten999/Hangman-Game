"""
    Filename: Hangman.py
    Creator: Keeten Sauer
    Purpose: A simple hangman game 
"""

import os
import random

# Attempt to load words from a local file so the word list is available
# to anyone who clones this repository. The file is `words.txt` next to
# this script (same folder). If the file is missing or empty, fall back
# to an internal list.
BASE_DIR = os.path.dirname(__file__)
WORDS_FILE = os.path.join(BASE_DIR, 'words.txt')

def load_words():
    try:
        with open(WORDS_FILE, 'r', encoding='utf-8') as f:
            words = [line.strip() for line in f if line.strip()]
            if words:
                return words
    except Exception:
        pass

    # Fallback list (keeps the game runnable without the file)
    return [
        'python', 'hangman', 'programming', 'challenge', 'computer',
        'keyboard', 'function', 'variable', 'condition', 'loop'
    ]


words = load_words()

while True:
    # Select a single random word from the loaded list
    chosen_word = random.choice(words).lower()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    guessed_letters = set()



    hangman_drawing = ["""
        -----
        |   |
            |
            |
            |
            |
    ---------
    """,
    """
        -----
        |   |
        O   |
            |
            |
            |
    ---------
    ""","""
        -----
        |   |
        O   |
        |   |
            |
            |
    ---------
    ""","""
        -----
        |   |
        O   |
        |\\  |
            |
            |
    ---------
    ""","""
        -----
        |   |
        O   |
       /|\\  |
            |
            |
    ---------
    ""","""
        -----
        |   |
        O   |
       /|\\  |
       /    |
            |
    ---------
    ""","""
        -----
        |   |
        O   |
       /|\\  |
       / \\  |
            |
    ---------
    """]

    print("--------------------")
    print("|  HANGMAN GAME!!  |")
    print("--------------------")

    while incorrect_guesses < max_incorrect_guesses:
        display_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_"

        print(hangman_drawing[incorrect_guesses])
        print(f"Word: {display_word}")
        print(f"Guessed Letters: {' '.join(sorted(list(guessed_letters)))}")
        print(f"Attempts Remaining: {max_incorrect_guesses - incorrect_guesses}")

        if "_" not in display_word:
            print("You Guessed The Word!!")
            break

        guess = input("Guess: ").lower()
        


        #make sure guess is one letter and numbers/ input validation
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter")

        #no repeats of letters
        if guess in guessed_letters:
            print("You already guessed that letter")
            continue

        guessed_letters.add(guess)

        if guess in chosen_word:
            print(f"Good guess {guess} is in the word")
        else:
            print(f"Sorry, {guess} is not in the word")
            incorrect_guesses += 1

    else:
        print(hangman_drawing[incorrect_guesses])
        print("GAME OVER")
        print(f"The Word Was {chosen_word}")
    
    choice = input("Do you want to play again? (y/n): ").lower()
    if choice == 'y':
        continue
    else:
        break
        