from .exceptions import *

#GuessAttempt: An attempt to guess a letter.
class GuessAttempt(object):
    pass
    
    attempt = word.perform_attempt('x')
    
    def __init__(self):
        pass
    
    def is_hit():
        '''
        for i in range(len(answer_word)):
                if answer_word[i].lower() == character.lower():
        return True''' 
        pass
    
    def is_miss():
        '''
        for i in range(len(answer_word)):
                if answer_word[i].lower() != character.lower():
        return False'''
        pass

#GuessWord: A word to guess. Is used by a HangmanGame to keep track of the word to guess.
class GuessWord(object): 
    pass
    
    word = GuessWord('xyz')
    
    def perform_attempt():
        '''
        if len(answer_word) == 0 or len(answer_word) != len(masked_word):
            raise InvalidWordException
        if len(character) != 1:
            raise InvalidGuessedLetterException
        new_masked = ''
        for i in range(len(answer_word)):
            if answer_word[i].lower() == character.lower():
                new_masked += answer_word[i].lower()
            else:
                new_masked += masked_word[i]
        return new_masked
        '''
#HangmanGame: the main interface for the user, the "general" game that will be used.
class HangmanGame(object):
    pass
