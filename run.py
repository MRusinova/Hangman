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


def play():
    """
    Playing the game function
    """
    word = pick_a_word()
    while True:
        guess = get_guess(word)
        if process_guess(guess, word):
            print('You win! Well Done!')
            break
        if lives_remaining == 0:
            print('You are Hung!')
            print('The Word was: ' + word)
            break


def print_word_with_blanks(word):
    """
    Compares the letter the player entered with every letter ofselected word.
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
    print('Lives remaining: ' + str(lives_remaining))
    guess = input('Guess a letter or a whole word?')
    return guess


def process_guess(guess, word):
    """
    To determine what to do in either case if the user enters whe whole word or a single letter.
    """
    if len(guess) > 1 and len(guess) == len(word):
        return whole_word_guess(guess, word)
    else:
        return single_letter_guess(guess, word)


def whole_word_guess(guess, word):
    """
    Function to handle if the user guessed the whole word
    """
    global lives_remaining
    if guess.lower() == word.lower():
        return True
    else:
        lives_remaining == lives_remaining - 1
        return False


def single_letter_guess(guess, word):
    """
    
    """
    global guessed_letters
    global lives_remaining
    if word.find(guess) == - 1:
        lives_remaining == 0
    guessed_letters = guessed_letters + guess.lower()
    if all_letter_guessed(word):
        return True
    return False


def all_letter_guessed(word):
    for letter in word:
        if guessed_letters.find(letter.lower()) == -1:
            return False
        return True

play()