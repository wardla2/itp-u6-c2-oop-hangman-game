from .exceptions import *

#GuessAttempt: An attempt to guess a letter.
class GuessAttempt(object):
    pass
    
    def __init__(self):
        pass
    
    def is_hit():
        '''new_masked = ''
           for i in range(len(answer_word)):
                if answer_word[i].lower() == character.lower():
                    new_masked += answer_word[i].lower()
                else:
                    new_masked += masked_word[i]
        return new_masked''' 
        pass
    
    def is_miss():
        pass

#GuessWord: A word to guess. Is used by a HangmanGame to keep track of the word to guess.
class GuessWord(object): 
    pass

#HangmanGame: the main interface for the user, the "general" game that will be used.
class HangmanGame(object):
    pass
