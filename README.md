# SI507-Project 1 README

Contents:
* SI507F17_project1_cards.py
* SI507F17_project1_tests.py
* code_description_507F17project1.txt
* helper_functions.py
* requirements.txt

Note: 3 errors were noted in the file SI507F17_project1_cards.py. Although the program runs, errors are tested and described in SI507F17_project1_tests.py

### requirements.txt
This file specifies the packages used to run all files in this folder. The Python version being used is 3.6

### helper_functions.py
This file is used with SI507F17_project1_cards.py to enable some of the web content functions

### code_description_507F17project1.txt
This file specifies exactly what is should happen in SI507_project1_cards.py. The file is in a paragraph format

### SI507_project1_tests.py
This file contains several unit tests to assess the functionality of SI507F17_project1_cards.py according to functionalities purported by code_description_507F17project1.txt.
Three errors have been identified in SI507F17_project1_cards.py, and the errors with their tests are described in this file.

### SI507_project1_cards.py
This program is a card game of War. The program is automated with 2 players, and besides the errors, requires no user input or change to the code.

The code consists of two classes:
* **Card**: This class creates a card with a rank and suit
* **Deck**: This class creates a deck made of 52 card instances. It also includes the following methods: pop_card, replace_card, shuffle, sort_cards, and deal_hand (discussed below)

and two functions:
* **play_war_game**: This is the function that plays the game. This function uses the Card and Deck instances to create a game between two players. Points are added up between players and a final score is determined. This function returns a tuple that includes the winning player (or TIE), the score of Player 1, and the score of Player 2
* **show_song**: This function searches iTunes for a song (default is "Winner"), and returns one instance of the results.

More Class details:

**Deck Class:**
Functions include:
* pop_card: (takes an input of the deck list index) Takes one card instance out from the deck list and returns the card instance
* replace_card: (takes an input of a card instance) Searches the whole deck to see if that card already exists in the deck. If it does not, takes the card instance and appends to the deck list
* shuffle: (takes no input) reorganizes the deck list
* sort_cards: (takes no input) should sort the remaining cards in the deck in the order of suit then rank. Returns a sorted list of the deck. [Error was found in this function, where it returns a sorted list of the entire deck, not only the remaining cards in the deck]
* deal_hand: (takes an input of the size of the hand) calls pop_card to pull out of the deck a number of cards equal to the size of the hand. Returns a list of the cards that appear in the hand. [Error was found in this function, where it calls pop_card based on an index of the hand_size. Therefore returns an error when the hand_size > approx 40] 
