"""
    Filename: Hangman.py
    Creator: Keeten Sauer
    Purpose: A simple hangman game 
"""



from random_word import RandomWords
r = RandomWords()

# Return a single random word
r.get_random_word()

print(r.get_random_word())