import random

words = ['chicken', 'dog', 'pasta', 'tomatoe', 'radio']
lives_remaining = 7
guessed_letters = ''

def pick_a_word():
    """
    Function to generate a random word from our list of strings
    """
    word_position = random.randint(0, len(words) - 1)
    return words[word_position]

def print_word_with_blanks(word):
    """
    Compares the letter the player entered with every letter of the randomly selected word.
    Displays if any of the guessed letters are in the generated word.
    """
    display_word = ''

    for letter in word:
        if guessed_letters.find(letter) > -1:
            display_word = display_word = letter
        else:
            display_word = display_word = '-'
    
    print(display_word)

def get_guess(word):
    """
    Function to tell how the player is doing when they try and guess
    Gives a print statement with lives remaining after guess
    Returning the user's guess
    """
    print_word_with_blanks(word)
    print(f'Lives remaining: {lives_remaining}')
    guess = input('Guess a letter or a whole word?')
    return guess
