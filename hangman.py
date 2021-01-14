import math
from random import random

def stick_figure(num, word_needed):
    if num == 5:
        return "o"
    elif num == 4:
        return "o'"
    elif num == 3:
        return "o;"
    elif num == 2:
        return "o;-"
    elif num == 1:
        return "o;-'"
    elif num == 0:
        return f"o;-;\nYou dead\nThe word you were looking for was '{word_needed}'"

def hangman():
    possible_words = ['array', 'list', 'dictionary', 'object', 'class', 'function']
    remaining_guesses = 6
    word_needed = possible_words[math.floor(random()*len(possible_words))]
    letters_guessed  = []
    currently_filled = []
    filled_string = ''
    word = ''
    for i in range(len(word_needed)):
        currently_filled.append("_")
    for ele in currently_filled:
        filled_string += ele + ' '
        word += ele
    else:
        while (remaining_guesses > 0 and word != word_needed):
            print(f"The word you need is: {filled_string}")
            print(f"Letters used: {letters_guessed}")
            guessed_letter = input("Guess a letter?\n")
            if guessed_letter not in letters_guessed:
                letters_guessed.append(guessed_letter)
                if guessed_letter in word_needed:
                    for i in range(len(word_needed)):
                        if guessed_letter == word_needed[i]:
                            if guessed_letter not in letters_guessed:
                                letters_guessed.append(guessed_letter)
                            currently_filled[i] = guessed_letter
                            new_filled_str = ''
                            new_word = ''
                            for ele in currently_filled:
                                new_filled_str += ele + ' '
                                filled_string = new_filled_str
                                new_word += ele
                                word = new_word
                            print("Correct")
                else:
                    remaining_guesses -= 1
                    print(f"Incorrect! You have {remaining_guesses} guesses remaining")
                    print(stick_figure(remaining_guesses, word_needed))
            else:
                print(f"'{guessed_letter}' has already been used")
    if word == word_needed:
        print("You win!")
hangman()