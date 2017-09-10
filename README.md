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
* Card: This class creates a card with a rank and suit
* Deck: This class creates a deck made of 52 card instances. It also includes the following methods: pop_card, replace_card, shuffle, sort_cards, and deal_hand (discussed below)

and two functions:
* play_war_game: This is the function that plays the game. This function uses the Card and Deck instances to create a game between two players. Points are added up between players and a final score is determined. This function returns a tuple that includes the winning player (or TIE), the score of Player 1, and the score of Player 2
* show_song: This function searches iTunes for a song (default is "Winner"), and returns one instance of the results.

More Class details:

Deck Class:
