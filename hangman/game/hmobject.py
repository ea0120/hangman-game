import random

class HmObj:
    """
        Data object the holds the hangman charactors.
   
    Attributes:
        value (list): The list that contain the hangman characters.
    """

    def __init__(self):
        """Constructs a new instance of Hangman Object.

        Args:
            self (HmObj): An instance of Hangman.
        """
        self.hangMan = [
            ' ___ ', 
            '/___\\',
            '\\   /',
            ' \\ / ',
            '  0  ',
            ' /|\\ ',
            ' / \\ ']

    def getHangManLen(self):
        """Returns the length of hangeman.

        Args:
            self (HmObj): An instance of Hangman.
        """
        return len(self.hangMan)

    def showMan(self):
        """Displays current parts of the hangman.
        
        Args:
            self (HmObj): An instance of Hangman.
        """
        #print the man
        for line in self.hangMan:
            print(line)

    def removeTopOfHM(self):
        """Removes top of hangMan.
        
        Args:
            self (HmObj): An instance of Hangman.
        """
        self.hangMan.pop(0)