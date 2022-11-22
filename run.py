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

print(pick_a_word())
