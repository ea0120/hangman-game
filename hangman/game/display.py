from game.hmobject import HmObj

class Display:
    """
    Display and get game information from the player.
   
    Attributes:
        value (int): .
    """
    
    def __init__(self):
        """Constructs a new instance of Display.

        guess(string): the player's input
        lettersGuessed(string): the letters the player has guessed.

        Args:
            self (Display): An instance of Display.
        """
        self.hmObj = HmObj()
        self.guess = ""
        self.lettersGuessed = ""

    def getHMCount(self):
        """Gets the hangMan's list length.

        Args:
            self (Display): An instance of Display.
        """
        return self.hmObj.getHangManLen()

    def showTheMan(self):
        """Shows hangman to player.

        Args:
            self (Display): An instance of Display.
        """
        self.hmObj.showMan()

    def askUserLetter(self):
        """asks for letter from user.

        Args:
            self (Display): An instance of Display.
        """
        #Get user letter
        self.guess = input("Guess a letter[a-z]: ")

    def checkAllLetters(self, secretWord, isPrint):
        """checks a letter's correctness.
       

        Args:
            self (Display): An instance of Display.
             secretWord(string): is the word that needs to be guessed
             isPrint(string): checks if a message needs to be printed.
        """
        #guess list
        self.lettersGuessed = self.lettersGuessed + self.guess
        wrongLetterCount = 0
        for letter in secretWord:
            if letter in self.lettersGuessed:
                if isPrint:
                    print(f"{letter}", end="")
            else:
                if isPrint:
                    print("_", end="")
                wrongLetterCount += 1
        #Move down for formating
        print()
        return wrongLetterCount

    def checkLetter(self, secretWord, failureCount):
        """checks the letter

        Args:
            self (Display): An instance of Display.
            secretWord(string): is the word that needs to be guessed
            failureCount(string): the count towards the player's failure.
        """ 
        #check if good letter
        if self.guess in secretWord:
            #if guess is correct
            print(f"Correct! There may be one or more {self.guess} in the secret word.")
        else:
            failureCount -= 1
            self.hmObj.removeTopOfHM()
            print(f"Sorry, that's incorect. There are no {self.guess} in the secret word. You have {failureCount} turn(s) left!")
        
        if self.checkAllLetters(secretWord, True) == 0:
            #push forward fail count if word is correct
            failureCount = 0
        #Return failureCount
        return failureCount

    def finalStat(self, secretWord):
        """look at the final state of the secret word

        Args:
            self (Display): An instance of Display.
            secretWord(string): is the word that needs to be guessed
        """
        #if win
        if self.checkAllLetters(secretWord, False) == 0:
            print(f"Yay! You did it! The secret word was {secretWord}. You won!")
        else:
            print(f"Sorry, you didn't win this time. The secret word was {secretWord}. Try Again!")
        