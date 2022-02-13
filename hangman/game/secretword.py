import random

class SecretWord:
    """A word is chosen from a dictionary of words. The word is chossen by 
       using a random number to get the value at that key.
    
    Attributes:
        value (dictionary): The dictionary and that contains the game words.
    """

    def __init__(self):
        """Constructs a new instance of SecretWord.

        Args:
            self (SecretWord): An instance of SecretWord.
        """
        self.secretWord_dic = {
            1: "heavenlyfather",
            2: "gosple",
            3: "joesephsmith",
            4: "jesus",
            5: "temple"
        }

    def getRandomWord(self):
        """Generates a new random word from dictionary and return 
           to main director class.
        
        Args:
            self (SecretWord): An instance of SecretWord.
        """
        rnum = random.randrange(1,5)
        return self.secretWord_dic[rnum]