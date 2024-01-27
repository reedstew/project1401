# File: Wordle.py

# """
# This module is the starter file for the Wordle assignment.
# BE SURE TO UPDATE THIS COMMENT WHEN YOU WRITE THE CODE.
# """

# Dev team: Reed & Jake

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS
LANG = 'FR'
def wordle():

    if LANG =='ENG':
    #Jake, 1/19/2024, 6:30pm: Defined function to take wotd and then check if it is in the dictionary or not.
        def enter_action(wotd):
            if wotd.lower() in FIVE_LETTER_WORDS:
                (gw.show_message("This is a temporary message for testing"))
            else:
                gw.show_message("Not in the word list")

        # Reed, 1/16/2024, 6pm: Defined function to call random word from by index number (0 - length of list minus one) from wordle list
        def choose_a_word():
            num = random.randint(0,(len(FIVE_LETTER_WORDS)-1))
            wotd = FIVE_LETTER_WORDS[num]
            wotd = wotd.upper()
            return wotd
        # Reed, 1/16/2024, 6:30pm: Defined function to place word chosen in first row. 
        # You will need to call a choose_a_word instance if you delete display_word later.
        def display_word():
            word = choose_a_word()
            i = 5
            for letter in word:
                gw.set_square_letter(0, i - N_COLS, letter)
                i+=1
                print(letter)

        gw = WordleGWindow()


        display_word()
        gw.add_enter_listener(enter_action)

    elif LANG == 'FR':
        french_file_path = "dictionnaire.txt"
    #Jake, 1/19/2024, 6:30pm: Defined function to take wotd and then check if it is in the dictionary or not.
        def enter_actionFR(mots):
            if mots.lower() in FIVE_LETTER_WORDS:
                (gw.show_message("Voici un message temporaire"))
            else:
                gw.show_message("Ce mot n'est pas dans la liste")

        # Reed, 1/16/2024, 6pm: Defined function to call random word from by index number (0 - length of list minus one) from wordle list
        def choose_a_french_word(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                french_words = [word.strip().upper() for word in file.readlines() if len(word.strip()) == 5]

            if not french_words:
                raise ValueError("No 5-letter words found in the French dictionary.")

            mots = random.choice(french_words)
            return mots

        # Reed, 1/16/2024, 6:30pm: Defined function to place word chosen in first row. 
        # You will need to call a choose_a_word instance if you delete display_word later.
        def display_wordFR():
            word = choose_a_french_word(french_file_path)
            i = 5
            for letter in word:
                gw.set_square_letter(0, i - N_COLS, letter)
                i+=1
                print(letter)

        gw = WordleGWindow()


        display_wordFR()
        gw.add_enter_listener(enter_actionFR)



# Startup code

if __name__ == "__main__":
    wordle()
