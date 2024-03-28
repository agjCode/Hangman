import random
import os
import Functions

#Initiates and sets up the format for Hangman
def Game():
    
    word = Functions.getWord()
    word = word.lower()
    lettersGuessed = '_' * len(word)
    tries = 0
    maxTries = 6


    ask = 'Make your guess: '
    while tries < maxTries and lettersGuessed != word:
        
        Functions.displayHangman(lettersGuessed, tries)
        guess = input(ask)

        if len(guess) != 1 or (not guess.isalpha()):
            ask = 'Invalid input, enter a character: '
        else:
            ask = 'Make your guess: '
            guess = guess.lower()
            if guess in word:
                
                lettersGuessed = list(lettersGuessed)
                for index, letter in enumerate(word):
                    if letter == guess:
                        lettersGuessed[index]= letter
                lettersGuessed = "".join(lettersGuessed)

            else:
                tries = tries + 1

        os.system('cls')
    
    Functions.displayHangman(lettersGuessed, tries)
    if tries == maxTries:
        print('YOU LOSE'.center(12))
    else:
        print('WINNER'.center(12))

                
                




