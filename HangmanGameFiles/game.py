#the secret word the play is trying to guess
from ast import Num
from random import random
#from secretWord import secretWord_dic
from HMobject import hangMan
lettersGuessed = ""
secretWord = "testing"
current_hangMan_index = 0

#The number of turns before the player loses
failureCount = 7

while failureCount > 0:

#main game mechanics
    #print(hangMan, sep = "\n")
    for line in hangMan:
        print(line)
    guess = input("Guess a letter[a-z]: ")


    if guess in secretWord:
        #if correct
        print(f"Correct! There may be one or more {guess} in the secret word.")
    else:
        failureCount -= 1
        print(f"Sorry, that's incorect. There are no {guess} in the secret word. You have {failureCount} turn(s) left!")


    #guess list
    lettersGuessed = lettersGuessed + guess
    wrongLetterCount = 0

    for letter in secretWord:
        if letter in lettersGuessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrongLetterCount += 1
            #hangMan.pop(0)

    #if win
    if wrongLetterCount == 0:
        print(f" Yay! You did it! The secret word was {secretWord}. You won!")
        break

else:
    print("Sorry, you didn't win this time. Try Again!")