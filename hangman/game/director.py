from game.display import Display
from game.secretword import SecretWord

class Director:
    """A object/class who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        secret word (string): the word the player is guessing.
        is_playing (boolean): Whether or not the game is being played.
        failureCount (int): The count towards the player's failed attempts.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        #Class Variables
        self.is_playing = True
        self.secretWord = ""

        #Object used in class
        self.swObj = SecretWord()
        self.disObj = Display()

        #The number of turns before the player loses
        self.failureCount = self.disObj.getHMCount()

        #Get Secret word
        self.secretWord = self.swObj.getRandomWord()

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            if self.failureCount <= 0:
                self.is_playing = False
            self.do_outputs()
            self.get_inputs()
            self.do_updates()
        self.disObj.finalStat(self.secretWord)

    def do_outputs(self):
        """Displays the hangMan state.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        self.disObj.showTheMan()

    def get_inputs(self):
        """Gets letter from user.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        self.disObj.askUserLetter()
        
    def do_updates(self):
        """Updates the hangMan status.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        self.failureCount = self.disObj.checkLetter(self.secretWord, self.failureCount)