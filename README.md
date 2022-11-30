# Hangman Game

Hangman Game is a Python terminal game, which runs in the Code Institute mock terminal on Heroku. You can read more about it on wikipedia https://en.wikipedia.org/wiki/Hangman_(game)

The computer generates a random word from a given list in the code and the game is for the user to guess what is the word. 


Here is my Hangman project https://hangman-ga.herokuapp.com/ 


<img src="README images/Screenshot (103).png" alt="">

## How to play


My Hangman Game is based on the classic pen and paper game that's usually played by two players. One player comes up with a word and puts dashes on a piece of paper for the empty spaces for the letters to be guessed. The second player then has to guess letters from the word and has limited guesses or until the player is "hanged". The first player has to put the correctly guessed letter in the correct position.

In my version the computer generates a random word from a given list with possible choices. The user than gets 7 'lives' to try and guess either a letter or the whole word. For every wrong entry or invalid input (such as blank space, symbol or a number) the player looses a live and can continue guessing until they loose all their lives which is when they get a message "You are HUNG" and the correct word displayed.
If the player guesses a correct letter said letter is put in the right position and the player doesn't loose a life. The user can also try and guess the whole word and if it's correct the word gets displayed in the terminal with the message "You win! Well done!"