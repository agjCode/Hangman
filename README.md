# Hangman
This folder has only 2 python files and a text file.
- [Game.py](https://github.com/agjCode/Hangman/blob/main/Game.py)
- [Functions.py](https://github.com/agjCode/Hangman/blob/main/Functions.py)

# Functions.py
Functions.py imports random package and has 2 defined functions.

## getWord()
- Opens and saves 'MissMeyers.txt' file contents onto a string, which then filters out words that are smaller than 3 letters and isn't purely constructed of letters.
- Will then pick a word at random of the filtered string and return it.
  
## displayHangman(lettersGuessed, tries)
- Takes string lettersGuessed and int tries then displays the current state of the hangman based on the tries value.
- Assumes that the max value of tries will be 6 and minimum 0.
- Under it will be the state of the progress towards guessing the letter based on lettersGuessed.

# Game.py
Game.py imports Functions and has 1 defined function
## Game()
- Initiates the hangman game.
- displayHangman() will not work as intended if tries and maxTries are changed.
- Will end when either the word is guessed or tries == maxTries
