import random

word_bank = ['banana', 'apple', 'grape', 'orange', 'kiwi', 'strawberry']
# word_bank = ['banana', 'apple', 'berry']


#display the unrevealed word as underscores with the same length
    # make a function that takes a parameter of the word and guesses
    #prompt the user to enter a letter
def hide_word(word):
    underscored_word = []
    for i in word:
        underscored_word.append('_')
    
    
    return underscored_word

# print(guess_letter('kiwi'))

def guess_letter():
    guess = input("What letter would you like to guess?")
    guess = guess.lower()
    return guess

def check_the_guess(guess, word):
    word_list = list(word)
    print(f"You guessed {guess}")

    # print(length_of_guess)
    if len(guess) > 1:
        print("Please enter a single character for example ('w')")
        # guess = input("What letter would you like to guess?")
        # guess_letter()
    elif guess in word_list:
        for idx, l in enumerate(word_list):
            # print(l)
            # print(idx)
            if guess == l:
                print("Correct")
                # change the index of the correctly guessed letter in hidden_word
                # print(hidden_word[word_list.index(guess)])
                hidden_word[idx] = guess
                # print(word_list.index(guess))
                print(hidden_word)
    else:
        return False


# Check every character in the word
# if any letter is an underscore you are not finished
# else you must have won
def check_win(hidden_word):
    hidden_word_string = ''.join(hidden_word)
    if hidden_word_string == word:
        print(f"Nice Job the word was {hidden_word_string}")
        return True
    else:
        return False

# def counter(counter = 5):
#     if counter == 0:
#         game_on = False 
    


# if the letter is in the word mark that letter in the underscores and show it
# if incorrect guess add to the counter
game_on = True

word = random.choice(word_bank)

hidden_word = hide_word(word)
hidden_word
counter = 0

stage1 = """
 ____
|    |
|    
|   
|    
|
-
"""
stage2 = """
 ____
|    |
|    O
|   
|    
|
-
"""
stage3 = """
 ____
|    |
|    O
|    |
|   
|
-
"""
stage4 = """
 ____
|    |
|    O
|   -|
|    
|
-
"""
stage5 = """
 ____
|    |
|    O
|   -|-
|    
|
-
"""
stage6 = """
 ____
|    |
|    O
|   -|-
|    /
|
-
"""
stage7 = """
 ____
|    |
|    O
|   -|-
|    /\
|
-
"""

while game_on == True:
    check_round = check_the_guess(guess_letter(), word)
    check_for_win = check_win(hidden_word)
    if (check_round) == False:
        counter += 1
    if counter == 5:
        print("GAME OVER")
        print(stage7)
        game_on = False
    elif counter == 0:
        print(stage1)
    elif counter == 1:
        print(stage2)
    elif counter == 2:
        print(stage3)
    elif counter == 3:
        print(stage4)
    elif counter == 4:
        print(stage5)
    elif counter == 5:
        print(stage6)
    if check_for_win == True:
        print("YOU WIN!!")
        game_on = False
        

