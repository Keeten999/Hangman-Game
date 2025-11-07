


import tkinter as tk
import random
from Hangman import load_words


class GameState:
    def __init__(self, words=None, max_incorrect=6):
        self.words = words or load_words()
        self.max_incorrect = max_incorrect
        self.reset()

    def reset(self):
        self.word = random.choice(self.words).lower()
        self.guessed = set()
        self.incorrect = 0

    @property
    def masked(self):
        return ' '.join([c if c in self.guessed else '_' for c in self.word])

    def guess(self, ch):
        ch = ch.lower()
        if not ch.isalpha() or len(ch) != 1:
            return 'invalid'
        if ch in self.guessed:
            return 'repeat'
        self.guessed.add(ch)
        if ch in self.word:
            return 'correct' if any(c not in self.guessed for c in self.word) else 'win'
        else:
            self.incorrect += 1
            return 'lose' if self.incorrect >= self.max_incorrect else 'incorrect'


def run_gui():
    state = GameState()
    root = tk.Tk()
    root.title('Hangman GUI')

    # ASCII-art frames (copied from Hangman.py)
    HANGMAN_FRAMES = [
        """
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
    """,
        """
        -----
        |   |
        O   |
        |   |
            |
            |
    ---------
    """,
        """
        -----
        |   |
        O   |
        |\  |
            |
            |
    ---------
    """,
        """
        -----
        |   |
        O   |
       /|\  |
            |
            |
    ---------
    """,
        """
        -----
        |   |
        O   |
       /|\  |
       /    |
            |
    ---------
    """,
        """
        -----
        |   |
        O   |
       /|\  |
       / \  |
            |
    ---------
    """
    ]

    hangman_label = tk.Label(root, text=HANGMAN_FRAMES[0], font=('Consolas', 10), justify='left')
    hangman_label.pack(padx=12, pady=(8, 6))


    word_label = tk.Label(root, text=state.masked, font=('Consolas', 28))
    word_label.pack(padx=12, pady=(6, 6))

    status = tk.Label(root, text=f'Attempts left: {state.max_incorrect - state.incorrect}    Guessed: ')
    status.pack(padx=12, pady=(0, 8))

    entry = tk.Entry(root, width=3, font=('Consolas', 18))
    entry.pack()

    result_label = tk.Label(root, text='', fg='green')
    result_label.pack(pady=(6, 6))

    def update_ui():
        word_label.config(text=state.masked)
        status.config(text=f'Attempts left: {state.max_incorrect - state.incorrect}    Guessed: {" ".join(sorted(state.guessed))}')
        hangman_label.config(text=HANGMAN_FRAMES[state.incorrect])

    def on_submit(event=None):
        ch = entry.get().strip()
        entry.delete(0, tk.END)
        res = state.guess(ch)
        if res == 'invalid':
            result_label.config(text='Enter a single letter', fg='orange')
        elif res == 'repeat':
            result_label.config(text=f'You already guessed "{ch}"', fg='orange')
        elif res == 'correct':
            result_label.config(text='Good guess', fg='green')
        elif res == 'incorrect':
            result_label.config(text=f'No "{ch}" in word', fg='red')
        elif res == 'win':
            update_ui()
            result_label.config(text=f'You win! Word: {state.word}', fg='green')
            play_again_button.pack(pady=(6,12))
            entry.config(state='disabled')
            return
        elif res == 'lose':
            update_ui()
            result_label.config(text=f'You lose. Word: {state.word}', fg='red')
            play_again_button.pack(pady=(6,12))
            entry.config(state='disabled')
            return
        update_ui()

    submit_btn = tk.Button(root, text='Guess', command=on_submit)
    submit_btn.pack(pady=(6, 4))

    def play_again():
        state.reset()
        entry.config(state='normal')
        result_label.config(text='')
        play_again_button.pack_forget()
        update_ui()

    play_again_button = tk.Button(root, text='Play again', command=play_again)

    entry.bind('<Return>', on_submit)

    update_ui()
    root.mainloop()


if __name__ == '__main__':
    run_gui()
