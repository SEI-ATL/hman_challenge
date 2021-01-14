import random
from words import words_list

def guess_word():
    word = random.choice(words_list)
    return word.upper()

def game(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words =[]
    tries = 4
    print("PLAY!!!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("guess a letter or word").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("you've already guessed that letter", guess)
            elif guess not in word:
                print(guess, "nope")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Nice", guess, "its in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list = "".join(word_as_list)
                    if "_" not in word_completion:
                        guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("you guessed this already",  guess)
            elif guess != word:
                print(guess,"not the word")
                tries -= 1
                guess_word.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("doesnt count")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("good job you guessed it")
    else:
        print("nope loser!!! the word is" + word)


    
                



