import random


class GameModel:
    """The model class for the word game.

    The model is responsible for the game logic and state.

    Attributes:
    ----------
    words : list
        A list of valid words to guess, the "dictionary"
    max_tries : int, default 6
        The maximum number of tries/guesses allowed
    target_word : str
        The word the player should try to guess
    try_count : int
        The number of tries/guesses made
    lines : list
        A list of tuples where each tuple contains a word and a list of checks.
        The word is a string and the checks is a list of integers where:
            INCORRECT_LETTER = 0: incorrect letter
            CORRECT_LETTER_NOT_POSITION = 1: correct letter, but in the wrong position
            CORRECT_LETTER_AND_POSITION = 2: correct letter in the correct position
    used_letters : set
        A set of letters that have been used in guesses
    """

    INCORRECT_LETTER = 0
    CORRECT_LETTER_NOT_POSITION = 1
    CORRECT_LETTER_AND_POSITION = 2

    def __init__(self, words: list[str], max_tries: int = 6):
        self.words = words
        self.max_tries = max_tries
        self.reset()

    def valid_word(self, word: str) -> bool:
        """Check if the word is valid, i.e. if it is in the dictionary.

        Parameters:
        ----------
        word : str
            The word to check

        Returns:
        -------
        bool
            True if the word is valid, False otherwise
        """
        return word in self.words
    
    def check_word(self, word: str) -> list[int]:
        """Check the word against the target word and return a list of checks.
        
        The checks are integers where:
            0 = incorrect letter
            1 = correct letter, but in the wrong position
            2 = correct letter in the correct position

        The enumeration values are also defined as class attributes:
            INCORRECT_LETTER = 0
            CORRECT_LETTER_NOT_POSITION = 1
            CORRECT_LETTER_AND_POSITION = 2

        Parameters:
        ----------
        word : str
            The word to check against the target word

        Returns:
        -------
        list[int]
            A list of checks for each letter in the word    
        """
        result = [GameModel.INCORRECT_LETTER for _ in word]
        remaining = list(self.target_word)
        # Check for correct letter and position. This has to be done before checking
        # for correct letter but wrong position to avoid double counting.
        for i, letter in enumerate(word):
            if letter == self.target_word[i]:
                result[i] = GameModel.CORRECT_LETTER_AND_POSITION
                remaining.remove(letter)
        # Check for correct letter but wrong position
        for i, letter in enumerate(word):
            if result[i] == 0 and letter in remaining:
                result[i] = GameModel.CORRECT_LETTER_NOT_POSITION
                remaining.remove(letter)
        return result

    def tries_left(self) -> bool:
        """Check if there are any tries left.

        Returns:
        -------
        bool
            True if there are tries left, False otherwise
        """
        return self.try_count < self.max_tries
    
    def has_won(self) -> bool:
        """Check if the player has won the game.

        Returns:
        -------
        bool
            True if the player has won, False otherwise
        """
        if not self.lines:
            return False
        checks = self.lines[-1][1]
        return all(check == GameModel.CORRECT_LETTER_AND_POSITION for check in checks)
    
    def play(self, word: str) -> list[int]:
        """Play a round of the game.

        Parameters:
        ----------
        word : str
            The word to play

        Returns:
        -------
        list[int]
            A list of checks for the word

        Raises:
        -------
        ValueError
            If there are no tries left
        """   
        if self.try_count >= self.max_tries:
            raise ValueError('No tries left')
        if not self.valid_word(word):
            return None
        self.try_count += 1
        self.used_letters = self.used_letters.union(set(word.upper()))
        checks = self.check_word(word)
        self.lines.append((word, checks))
        return checks

    def reset(self) -> None:
        """Reset the game state.
        """
        self.target_word = random.choice(self.words)
        self.try_count = 0
        self.lines = []
        self.used_letters = set()


class GameView:
        """The view class for the wordle style game.

        The view is responsible for displaying the game state to the user.

        Attributes:
        ----------
        display_used : bool
            If True, the set of used letters are printed after each move
        
        Parameters:
        ----------
        display_used : bool, default False
            If True, the set of used letters are printed after each move
              
        """
    
        def __init__(self, lang_code: str = 'sv', display_used: bool = False):
            self.lang_code = lang_code
            self.display_used = display_used
    
        def display_welcome(self):
            """Display a welcome message with the rules of the game.
            """
            print(f'\n\nWelcome to the game of wordle! (language: {self.lang_code})')
            print('I am thinking of a five-letter word.')
            print('You have 6 tries to guess the word.')
            print('After each guess, you will receive feedback on the correctness of the letters.')
            print('The feedback is given as follows:')
            print(' *X*  - correct letter in the correct position')
            print(' (X)  - correct letter, but in the wrong position')
            print('  X   - incorrect letter')
            print('\nGood luck!\n\n')


        def display_lines(self, lines: list[(str, list[int])]) -> None:
            """"Draw a grid with the words and checks as in the example below.

            +-----+-----+-----+-----+-----+
            | *S* |  T  | (A) | (R) |  T  |
            +-----+-----+-----+-----+-----+

            Here, the target word is "spray" and the user has guessed "start".
            The user has guessed the first letter correctly and in the correct position,
            the third and fourth letters are correct but in the wrong position.

            Parameters:
            ----------
            lines : list
                A list of tuples where each tuple contains a word and a list of checks.
                The word is a string and the checks is a list of integers where:
                    0 = incorrect letter
                    1 = correct letter, but in the wrong position
                    2 = correct letter in the correct position
            """
            if not lines:
                return
            print('+-----+-----+-----+-----+-----+')
            for word, checks in lines:
                print('|', end='')
                for i, letter in enumerate(word):
                    letter = letter.upper()
                    if checks[i] == GameModel.CORRECT_LETTER_AND_POSITION:
                        print(f' *{letter}* |', end='')
                    elif checks[i] == GameModel.CORRECT_LETTER_NOT_POSITION:
                        print(f' ({letter}) |', end='')
                    else:
                        print(f'  {letter}  |', end='')
                print()
            print('+-----+-----+-----+-----+-----+')

        def display_used_letters(self, used_letters: set[str]) -> None:
            """Display the set of used letters. 
            
            If the set is empty or if the display_used attribute is False, nothing is printed.

            Parameters:
            ----------
            used_letters : set
                A set of letters that have been used in guesses
            """
            if not used_letters or not self.display_used:
                return
            print('Used letters:', ' '.join(used_letters))

        def display_winning_message(self):
            """Display a winning message.
            """
            print('\n\n🏆 Congratulations 🏆 You won! Perhaps another game?\n\n')

        def display_game_over(self, target_word: str):
            """Display a game over message with the target word.
            """
            print('\n\n😢 Game over! The target word was:', target_word, '\n\n')

        def display_invalid_word(self, bad_word: str):
            """Display a message informing that the entered word is incorrect.

            Parameters:
            ----------
            bad_word : str
                The invalid word 
            """
            print('Invalid word:', bad_word)

        def get_word_input(self) -> str:
            """Get a word input from the user.

            Returns:
            -------
            str
                The input from the user
            """
            return input('Enter a word:').lower()
        

class GameController:
    """The controller class for the word game.

    The controller is responsible for the game flow and communication between the model and the view.

    Attributes:
    ----------
    model : GameModel
        The model for the game
    view : GameView
        The view for the game

    Parameters:
    ----------
    model : GameModel
        The model for the game
    view : GameView
        The view for the game
    """
        
    def __init__(self, model: GameModel, view: GameView):
        self.model = model
        self.view = view

    def play(self):
        """Play the game.
        """
        self.model.reset()
        self.view.display_welcome()
        while self.model.tries_left():
            self.view.display_lines(self.model.lines)
            self.view.display_used_letters(self.model.used_letters)
            word = self.view.get_word_input()
            if not self.model.valid_word(word):
                self.view.display_invalid_word(word)
                continue
            self.model.play(word)
            if self.model.has_won():
                self.view.display_lines(self.model.lines)
                self.view.display_winning_message()
                break
        else:
            self.view.display_lines(self.model.lines)
            self.view.display_game_over(self.model.target_word)



