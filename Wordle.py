# File: Wordle.py

# """
# This module is the starter file for the Wordle assignment.
# BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
# """

# Dev team: Reed & Jake

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():

    def enter_action(s):
        gw.show_message("You have to implement this method.")

    # Reed, 1/16/2024, 6pm: Defined function to call random word from by index number (0 - length of list minus one) from wordle list
    def choose_a_word():
        num = random.randint(0,(len(FIVE_LETTER_WORDS)-1))
        wotd = FIVE_LETTER_WORDS[num]
        return wotd
    
    def display_word():
        word = choose_a_word()
        i = 1
        for letter in word:
            print(letter)
            gw.set_square_letter(0, N_COLS - i, letter)
            i += 1

    gw = WordleGWindow()
    display_word()
    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    wordle()
