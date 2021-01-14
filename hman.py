import random #allows us to use choice
from math import floor

#my solution
# diff_requirements = ["python", "javascript", "html", "css", "react", "mongoDB", "api", "frontend", "backend", "fullstack"]
# words = random.choice(diff_requirements)
# print(words)

# guess = ""

# turns_left = 7

# while turns_left > 0:
#     lost = 0
    
#     for letter in words:
#         if letter in guess:
#             print(letter)
#         else:
#             print("_   each dash shows how many letter you need")
#             lost += 1
            
#     if lost == 0:
#         print("you win great job")
        

#     user_input = input("Guess a letter in the job requirement: ")
#     guess += user_input

#     if guess not in words:
#         turns_left -= 1
#         print("letter was wrong, you have:", turns_left , " turns left")
        
#         if turns_left == 0:
#             print("you lost try again")

#class solution

# Initialize game

secret_word = ""
letters_left = 0
hangman_guesses_left = 6
letters_guessed = []
errors = 0
underscored_secret_word = ""
secret_words = ["development", "random", "postman", "mountain", "python", "wrong", "javascript", "software", "engineer"]
# visual variables
hangman1 = '''
______
|    |
|    O
|
|
|__________
'''
hangman2 = '''
______
|    |
|    O
|    |
|
|__________
'''
hangman3 = '''
______
|    |
|    O
|   /|
|
|__________
'''
hangman4 = '''
______
|    |
|    O
|   /|\\
|
|__________
'''
hangman5 = '''
______
|    |
|    O
|   /|\\
|   /
|__________
'''
hangman6 = '''
______
|    |
|    O
|   /|\\
|   / \\
|__________
'''
hangman_table = [
  f'\n{hangman6}\n',
  f'\n{hangman5}\n',
  f'\n{hangman4}\n',
  f'\n{hangman3}\n',
  f'\n{hangman2}\n',
  f'\n{hangman1}\n'
]

#planning 
#functions

#game init 
def game_init():
    global secret_word
    global letters_left
    global hangman_guesses_left
    global letters_guessed
    global errors
    global underscored_secret_word
    
    random_index = floor(random() * 6 )
    secret_word = secret_words[random_index]
    letters_left = len(secret_word)
    hangman_guesses_left = 6
    letters_guessed = []
    
    i = 0
    while i < len(secret_word):
        underscored_secret_word = underscored_secret_word + "_"
        i += 1
        
def win():
    print('You won!')
    print(f"the word was {secret_word}")
    
def lose():
    print("HMAN: :(")
    print(f"The secret word was {secret_word}")
    
def add_to_guesses(guess):
    letters_guessed.append(guess)
    
def success(guess):
    global underscored_secret_word
    global win
    print("Correct")
    add_to_guesses(guess)
    index = 0
    for letter in secret_word:
        if letter == guess:
        # handle the case for the first letter in the secret word is the guess
            if index == 0:
                underscored_secret_word = guess + underscored_secret_word[1:] #apple -> a_ _ _ _ _
        # handle the case for when the guessed letter is not the first or last letter
            elif index < (len(secret_word) - 1 ):
                underscored_secret_word = underscored_secret_word[0: (index * 2)] + guess + " " + underscored_secret_word[(index * 2 + 2)]
            else:
                underscored_secret_word = underscored_secret_word[:-2] + guess
        index += 1
        
        #check if all letters have been guessed, and if so run win() otherwise , we'll continue the game
        for letter in underscored_secret_word:
            if letter == '_':
                continue_game()
                return
        win()
        
def print_hangman(incorrect_guesses_left):
    print(hangman_table[hangman_guesses_left])
    
def failure(guess):
    global hangman_guesses_left
    add_to_guesses(guess)
    hangman_guesses_left -= 1
    print_hangman(hangman_guesses_left)
    continue_game()
    
def already_guessed():
    print('You already guessed that')
    continue_game()
    
def continue_game():
    global errors
    print(f"You have {hangman_guesses_left} guesses left")
    print(f"You have guessed: {letters_guessed}")
    print(f"You word you need: {underscored_secret_word}")
    #can user continue to make guesses or is the game over
    if hangman_guesses_left > 0:
        guess = input('Guess a letter: \n').lower()
        if guess == secret_word:
            win()
            return
        #handle special cases - if the user gets a non letter char or multiople letter
        # we can allow one error before counting it against the user
        if len(guess) > 1 and errors < 1 :
            print('it looks like you accidentally entered the wrong character or you guessed the wrong word')
            errors += 1
            continue_game()
            return
        try:
            int(guess)
            print('it looks like you accidentally enter a number')
            errors += 1
            continue_game()
            return
        except ValueError:
            pass
        
        if guess in letters_guessed:
            already_guessed()
            return
        
        for letter in secret_word:
            if letter == guess:
                success(guess)
                return
            failure(guess)
            return
    else:
        lose()
        
# game loop that is going to continue running the game, call game_init() and initially run the continue game().
#Prompt the user to see if they want to continue playing

looping = True
game_init()
continue_game()

while looping:
    should_continue = input('would you like to play again? yes or no \n').lower()
    if should_continue == "yes" or should_continue == "y":
        game_init()
        continue_game()
    elif should_continue == "no" or should_continue == "n":
        print("thanks for playing")
        looping = False
    else:
        print("I'm no sure if you mean yes or no. \n")
            
    
        
        
    