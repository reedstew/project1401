# File: Wordle.py

# """
# This is the Wordle Game code
# """

# Dev team: Reed & Jake

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():

    #Jake, 1/19/2024, 6:30pm: Defined function to take wotd and then check if it is in the dictionary or not.
    def enter_action(user):
        nonlocal i
        # see what the user guessed

        if user.lower() in FIVE_LETTER_WORDS:
            # (gw.show_message("This is a temporary message for testing"))
            # First try congrats
            if user == wotd:
                gw.show_message("WOW! You got it first try!")
            else:
                setcolor(user)
        else:
            gw.show_message("Not in the word list")

        i+=1
        gw.set_current_row(i)

    # Reed, 1/26/2024, 3:30pm: Defined function to set the color of the tiles based on the guess
    def setcolor(user):
        # loop through the squares and match the rows.
        for ea in user:
            if user[ea] == wotd[ea]:
                gw.set_square_color(i,(ea+1),CORRECT_COLOR)
            elif user[ea] in wotd:
                gw.set_square_color(i,(ea-1),PRESENT_COLOR)
            else:
                gw.set_square_color(i,(ea-1),MISSING_COLOR)


    # Reed, 1/16/2024, 6pm: Defined function to call random word from by index number (0 - length of list minus one) from wordle list
    def choose_a_word():
        num = random.randint(0,(len(FIVE_LETTER_WORDS)-1))
        wotd = FIVE_LETTER_WORDS[num]
        wotd = wotd.upper()
        print(wotd)
        return wotd
    
    # Reed, 1/16/2024, 6:30pm: Defined function to place word chosen in first row. 
    # You will need to call a choose_a_word instance if you delete display_word later.
    # def display_word():
    #     word = choose_a_word()
    #     i = 5
    #     for letter in word:
    #         gw.set_square_letter(0, i - N_COLS, letter)
    #         i+=1
    #         print(letter)

    #a counter to keep track of the row we are on
    i = 0

    #instantiate
    gw = WordleGWindow()

    wotd = choose_a_word()
    # display_word()
    gw.add_enter_listener(enter_action)


# Startup code

if __name__ == "__main__":
    wordle()
