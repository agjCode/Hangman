import random

#Returns word as a string that is chosen at random from file "MissMyeres.txt"
def getWord():
    file = open(r'MissMeyers.txt', 'r')
    

    oldWords = file.read()
    oldWords = oldWords.split()

    words = [aWord for aWord in oldWords if len(aWord) >= 3 and aWord.isalpha()]
    word = random.choice(words)
    
    file.close()
    return word

#Display the current state of the "Hangman"
#Assumes max tries is 6
def displayHangman(lettersGuessed, tries):
    
    print('---------')
    print('|       |')
    
    print('|      ', end='') 
    print('\\O/' if tries > 3 else ' O/' if tries > 2 else ' O' if tries > 0 else ' ')
    print('|       ', end='')
    
    print('|' if tries > 1 else ' ')
    print('|      ', end='')
    print('/ \\' if tries > 5 else '  \\' if tries > 4 else ' ')

    print('|')
    print('|')
    print(lettersGuessed.center(12))