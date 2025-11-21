import requests
import os
import random
import certifi

# Attempt to load words from a local file so the word list is available
# to anyone who clones this repository. The file is `words.txt` next to
# this script (same folder). If the file is missing or empty, fall back
# to an internal list.

BASE_DIR = os.path.dirname(__file__)
WORDS_FILE = os.path.join(BASE_DIR, 'words.txt')

def api_key():
    # Pick a random starting letter
    start_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
    url = f"https://api.datamuse.com/words?max=200&md=d&sp={start_letter}*"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        words = [item['word'] for item in data if 'defs' in item]
        random.shuffle(words)
        return words
    else:
        print(f"Error: {response.status_code}")
        return []

words = api_key()

def main():
    win = 0
    played = 0
    while True:
        # Select a single random word from the loaded list
        chosen_word = random.choice(words).lower()
        incorrect_guesses = 0
        max_incorrect_guesses = 6
        guessed_letters = set()
        played += 1
        #drawing array
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
        #print out heading/title
        print("--------------------")
        print("|  HANGMAN GAME!!  |")
        print("--------------------")


        #loop for game to continue as long as the inccorect guesses are less than the max guesses allowed
        while incorrect_guesses < max_incorrect_guesses:
            display_word = ""
           
            for letter in chosen_word:
                if letter in guessed_letters:
                    display_word += letter + " "
                else:
                    # diplay _ for each undiscovered letter in the word
                    display_word += "_"

            #print out the drawing in the array number equivalant to the number of incorrect guesses
            print(hangman_drawing[incorrect_guesses])
            #print the current word (as letters are guessed they will be inputed)
            print(f"Word: {display_word}")
            #display a list of already guessed letters
            print(f"Guessed Letters: {' '.join(sorted(list(guessed_letters)))}")
            #give # of attempts remaining
            print(f"Attempts Remaining: {max_incorrect_guesses - incorrect_guesses}")

            #if no _ remain - word is guessed
            if "_" not in display_word:
                print("You Guessed The Word!!")
                win += 1
                break
            #get a guess and make it lower case
            guess = input("Guess: ").lower()

            # make sure guess is one letter and not numbers/ input validation
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid input. Please enter a single letter")
                continue

            # no repeats of letters
            if guess in guessed_letters:
                print("You already guessed that letter")
                continue
            
            #add the new letter to guessed letters list
            guessed_letters.add(guess)
            #display based on input
            if guess in chosen_word:
                print(f"Good guess {guess} is in the word")
            else:
                print(f"Sorry, {guess} is not in the word")
                incorrect_guesses += 1
        #game over response/ give actual word
        else:
            print(hangman_drawing[incorrect_guesses])
            print("GAME OVER")
            print(f"The Word Was {chosen_word}")
        #replay choice
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice == 'y':
            continue
        else:
            #display win rate
            print(f"Win rate was: {(win/played)*100}%")
            break


if __name__ == "__main__":
    main()
        