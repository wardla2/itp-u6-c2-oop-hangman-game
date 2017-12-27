from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = []

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
        
      def guess_letter(game, letter):
        if game['masked_word'].find('*') == -1 or game['remaining_misses'] <= 0:
            raise GameFinishedException
        if len(letter) != 1 or not letter.isalpha():
            raise InvalidGuessedLetterException
            
        old_masked = game['masked_word']
        game['masked_word'] = _uncover_word(game['answer_word'], game['masked_word'], letter)
        game['previous_guesses'].append(letter.lower())
        
        if old_masked == game['masked_word']:    ## no unmasking; this was a bad guess
            game['remaining_misses'] -= 1
        if game['masked_word'].find('*') == -1:
            raise GameWonException
        if game['remaining_misses'] == 0:   
            raise GameLostException
        '''
#HangmanGame: the main interface for the user, the "general" game that will be used.
class HangmanGame(object):
    pass
    
    WORD_LIST = ['rmotr', 'python', 'awesome']
    
    def _select_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException
    i = random.randint(0, len(list_of_words) - 1)
    print(list_of_words[i])
    return list_of_words[i]
    
    def __init__(self, word_list=['Python', 'rmotr'], num_of_guesses=5):
        passs
        
    def _mask_word(word):
    if len(word) == 0:
        raise InvalidWordException
    return '*'*(len(word))
    
    def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }
