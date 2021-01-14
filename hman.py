# IMPORTED RANDOM FROM LIBRARY TO GET RANDOM WORD IN TUPLE
import random


# TUPLE OF WORDS TO PULL FROM
words_list = ['jackets','chipmunk','republicans','tuple','lumberjacks','numbed','paycheck','vanquish']

# SETTING THE RANDOM WORD ONCE hmna.py GETS RAN IN TERMINAL
random_word = words_list[random.randrange(len(words_list))]
# print(random_word) # working -> generates random word

# GLOBAL VALUES BEING STORED (HIDDEN WORD, LETTERS ALREADY GUESSED AND NUMBER OF WRONG GUESSES )
hidden_word = ''
already_guessed = []
num_wrong_guesses = 0

# FUNCTION THAT CREATES THE HIDDEN WORD
def hide_word(random_word):
        global hidden_word
        hidden_word = '_' * len(random_word)
# print(hidden_word) # working -> displays ['_','_','_','_','_'] for word

# FUNCTION THAT CHECK THE STATUS OF HOW MANY WRONG GUESSES THE USER HAS
def check_status(num_wrong_guesses):
    if num_wrong_guesses != 6:
        # print(num_wrong_guesses)
        return 'alive'
    else:
        print('\nYOU LOST!\nThank you for playing!\n\n\n')
        quit()

# CHECKS THE CURRENT VALUE OF THE HIDDEN WORD TO SEE IF IT MATCHES THE ACTUAL RANDOM WORD
def check_word(word):

    if word == '_' * len(hidden_word):
        pass
    if word == random_word:
        print('you won!')
        quit()
    else:
        pass

# CHECKS TO SEE IF THE LETTER GUESS IS IN THE WORD, IS NOT IN THE WORD, IS NOT A LETTER, IS THE WHOLE WORD, IS ALREADY GUESSED OR IF THE USER WOULD LIKE TO QUIT.
def letter_guessed(letter):
    global num_wrong_guesses
    global hidden_word
    
    if letter == '':
        print('Please type a letter.')
    elif letter == 'quit':
        print(f'\n\nThanks for playing!')
        quit()
    elif letter in already_guessed:
        print('\nOops, try another letter.\n\n')
        
    elif letter == random_word:
        print('\nGreat guess!\nYou WIN!\n\n\n')
        quit()
    elif letter not in random_word:
        print(f'\nSorry, {letter} is not in the word.\nYou have {5 - num_wrong_guesses} wrong answers left.')
        already_guessed.append(letter)
        new_num = int(num_wrong_guesses) + 1
        num_wrong_guesses = num_wrong_guesses + 1


        # SETS THE HANGMAN ASCII DEPENDING ON THE NUMBER OF WRONG GUESS THE USER CURRENTLY HAS
        if num_wrong_guesses == 6:
            print(' \n _________\n|         |\n|         O\n|        -|-\n|        / \ \n-')
        elif num_wrong_guesses == 5:
            print(' \n _________\n|         |\n|         O\n|        -|-\n|        /\n|\n-')
        elif num_wrong_guesses == 4:
            print(' \n _________\n|         |\n|         O\n|        -|-\n|\n|\n-')
        elif num_wrong_guesses == 3:
            print(' \n _________\n|         |\n|         O\n|        -|\n|\n|\n-')
        elif num_wrong_guesses == 2:
            print(' \n _________\n|         |\n|         O\n|         |\n|\n|\n-')
        elif num_wrong_guesses == 1:
            print(' \n _________\n|         |\n|         O\n|        \n|\n|\n-')
        elif num_wrong_guesses == 0:
            print(' \n _________\n|         |\n|         \n|        \n|\n|\n-')

        print(f'\n{hidden_word}')
        print(f'LETTERS ALREADY GUESSED:\n{already_guessed}')
        check_status(new_num)

    elif letter in random_word:
        already_guessed.append(letter)
        index = random_word.find(letter)
        split_hidden_word = list(hidden_word)
        split_hidden_word[int(index)] = letter
        hidden_word = "".join(split_hidden_word)
        check_word(hidden_word)
        print(f'\n{hidden_word}')
        print(f'LETTERS ALREADY GUESSED:\n{already_guessed}')
        

# STARTS THE GAME AND RUNS UNTIL THE NUMBER OF WRONG GUESSES MATCHES MAX NUMBER OF WRONG GUESSES SET BY DEV
def start_game():
    name = input('\n\nWhats is your name?  ')
    print(f'\nHello {name}!')
    print('----------------------------------------------------------------------------')
    print(f'\n Welcome to HMan, {name}, we have stored a word for you\n and your job is to guess the word before you hang the\n poor stick person. When prompted, choose a letter that\n you think is in the hidden word. If you are right, we\n will give you that letter, but if you are wrong...\n\n Hangtime! 😈')
    print('----------------------------------------------------------------------------')
    
    
    # CONFIRMS IF THE PLAYER WANTS TO PLAY OR QUIT
    def ready():
        answer = input("\n\nAre you ready? y/n     ")
        if answer == "y":
            while num_wrong_guesses != 6:
                hide_word(random_word)
                print('\n\n----------------------------------------------------------------')
                print(f'Your word has {len(hidden_word)} letters, here is your word: \n\n                         {hidden_word}')
                print('----------------------------------------------------------------')
                print(f'THIS SHOULD NOT PRINT: {random_word}')
                letter = input('\n\nWhat is your letter?      ')
                letter_guessed(letter)
                check_status(num_wrong_guesses)
            
        elif answer == 'n':
            pass
    ready()

# ENVOKES THE BEGINNING OF THE GAME
start_game()

# * Prompt the user to enter a letter.

# * If the letter is in the word, mark it as revealed and visually display that letter in the word.
# * If the letter is incorrect, draw another part onto the stick person.