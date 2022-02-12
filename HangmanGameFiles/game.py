#the secret word the player is trying to guess
from secretWord import getRandomWord as getW
from HMobject import hangMan
lettersGuessed = ""
secretWord = ""
current_hangMan_index = 0

#The number of turns before the player loses
failureCount = len(hangMan)

secretWord = getW()

#main game mechanics
while failureCount > 0:
    #print the man
    for line in hangMan:
        print(line)

    #Get user letter
    guess = input("Guess a letter[a-z]: ")

    #check if good letter
    if guess in secretWord:
        #if correct
        print(f"Correct! There may be one or more {guess} in the secret word.")
    else:
        failureCount -= 1
        hangMan.pop(0)
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
    
    #Move down for formating
    print()

    #if win
    if wrongLetterCount == 0:
        print(f" Yay! You did it! The secret word was {secretWord}. You won!")
        break

else:
    print("Sorry, you didn't win this time. Try Again!")