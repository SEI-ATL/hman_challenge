import math
from random import random

def stick_figure(num):
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
        return 'o;-;\nYou dead'

def hangman():
    possible_words = ['array', 'list', 'dictionary', 'object', 'class', 'function']
    remaining_guesses = 6
    word_needed = possible_words[math.floor(random()*len(possible_words))]
    letters_guessed  = []
    currently_filled = []
    filled_string = ''
    for i in range(len(word_needed)):
        currently_filled.append("_")
    for ele in currently_filled:
        filled_string += ele + ' '
    while (remaining_guesses > 0):
        print(f"The word you need is: {filled_string}")
        print(f"Letters used: {letters_guessed}")
        guessed_letter = input("Guess a letter?\n")
        for i in range(len(word_needed)):
            if guessed_letter == word_needed[i]:
                letters_guessed.append(guessed_letter)
                currently_filled[i] = guessed_letter
                new_filled_str = ''
                for ele in currently_filled:
                    new_filled_str += ele + ' '
                    filled_string = new_filled_str
                print("Correct")
            else:
                remaining_guesses -= 1
                stick_figure(remaining_guesses)
        

    

hangman()