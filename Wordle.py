# File: Wordle.py

# """
# This is the Wordle Game code
# """

# Dev team: Reed & Jake

import random
from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

# Change colors for colorblind:
CORRECT_COLOR = "#1F7DF1"
PRESENT_COLOR = "#F19A1F"
# Initiate LANG variable
LANG = 'ENG'

def wordle():
    global LANG

    lang_input = input('Language English or Francais?: ')
    if lang_input[0].lower() == 'f':
        LANG = 'FR'
    elif lang_input[0].lower() == 'e':
        LANG = 'ENG'

    if LANG =='ENG':
        #track if first try
        first = 0

        #Jake, 1/19/2024, 6:30pm: Defined function to take wotd and then check if it is in the dictionary or not.
        def enter_action(user):
            nonlocal iRow
            nonlocal first
            # see what the user guessed
            if user.lower() in FIVE_LETTER_WORDS:
                    # (gw.show_message("This is a temporary message for testing"))
                # First try congrats
                if user == wotd and first == 0:
                    gw.show_message("First try!!! Wow, you should invest in stocks today!")
                elif user == wotd:
                    gw.show_message("WOW! You are amazing!")
                    set_color(user)
                else:
                    set_color(user)
                iRow += 1
                gw.set_current_row(iRow)
            else:
                gw.show_message("Not a word. Try again, and read more books!")
            first += 1

        # Reed, 1/26/2024, 3:30pm: Defined function to set the color of the tiles based on the guess
        def set_color(user):
            #help with duplicates
            track = {letter: 0 for letter in user}
            # loop through the squares and match the rows.
            for ea in range(len(user)):
                if user[ea] == wotd[ea]:
                    gw.set_square_color(iRow,ea,CORRECT_COLOR)
                    track[user[ea]] += 1
                elif user[ea] in wotd and track[user[ea]] == 0:
                    gw.set_square_color(iRow,ea,PRESENT_COLOR)
                    track[user[ea]] += 1
                else:
                    gw.set_square_color(iRow,ea,MISSING_COLOR)
            print(track)

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
        iRow = 0
        #instantiate
        gw = WordleGWindow()
        wotd = choose_a_word()
            # display_word()
        gw.add_enter_listener(enter_action)
        wordle()
        
# Jake, 1/27/2024, 1:20pm All of the french stuff is added I added the same thing but it pulls from the french dictionary. To start the program it prompts what language.... I dont know if this is how we want to do it
    elif LANG == 'FR':

        with open("dictionnaire.txt", 'r', encoding='utf-8') as file:
            french_words = [word.strip().upper() for word in file.readlines() if len(word.strip()) == 5]

        if not french_words:
            raise ValueError("No 5-letter words found in the French dictionary.")

        def enter_actionFR(mots):
            if mots.upper() in french_words:
                gw.show_message("Voici un message temporaire")
            else:
                gw.show_message("Ce mot n'est pas dans la liste")

            gw.change_current_row()

        def choose_a_french_word():
            return random.choice(french_words)

        def display_wordFR():
            mots = choose_a_french_word()
            i = 5
            for letter in mots:
                gw.set_square_letter(0, i - N_COLS, letter)
                i += 1
                print(letter)
            return mots

        # Assuming the following lines are part of your program

        gw = WordleGWindow()

 #       display_wordFR()
        

        # Assuming your event listener setup is within the graphics module
        gw.add_enter_listener(lambda mots: enter_actionFR(mots))
        wordle()
       




# Startup code

if __name__ == "__main__":
   wordle()
