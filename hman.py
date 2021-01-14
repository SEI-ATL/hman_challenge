import random


# * Store a list (or tuple) of 5 to 10 words in your script.
words_list = ['jackets','chipmunk','republicans','tuple','lumberjacks','numbed','paycheck','vanquish']

# * Randomly choose a word from this list as the secret word.
random_word = words_list[random.randrange(len(words_list))]
# print(random_word) # working -> generates random word

# * Display the unrevealed word as underscores (with the same length.)
hidden_word = ''
hang_man = ''
already_guessed = []
num_wrong_guesses = 0

# TEST TO FIND OUT THE MAX AMOUNT OF TIMES TO ASK INPUT
# def test():
#     summ = len(random_word) + 6
#     print(summ)
# test()

def hide_word(random_word):
        global hidden_word
        hidden_word = '_' * len(random_word)
# print(hidden_word) # working -> displays ['_','_','_','_','_'] for word

def check_status(num_wrong_guesses):
    if num_wrong_guesses != 6:
        # print(num_wrong_guesses)
        return 'alive'
    else:
        print('\nYOU LOST!\nThank you for playing!\n\n\n')
        quit()

def check_word(word):

    if word == '_' * len(hidden_word):
        pass
    if word == random_word:
        print('you won!')
        quit()
    else:
        pass

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

        if num_wrong_guesses == 6:
            print(' \n_________\n|         |\n|         O\n|        -|-\n|        / \ \n-')
        elif num_wrong_guesses == 5:
            print(' \n_________\n|         |\n|         O\n|        -|-\n|        /\n|\n-')
        elif num_wrong_guesses == 4:
            print(' \n_________\n|         |\n|         O\n|        -|-\n|\n|\n-')
        elif num_wrong_guesses == 3:
            print(' \n_________\n|         |\n|         O\n|        -|\n|\n|\n-')
        elif num_wrong_guesses == 2:
            print(' \n_________\n|         |\n|         O\n|         |\n|\n|\n-')
        elif num_wrong_guesses == 1:
            print(' \n_________\n|         |\n|         O\n|        \n|\n|\n-')
        elif num_wrong_guesses == 0:
            print(' \n_________\n|         |\n|         \n|        \n|\n|\n-')

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
        

def start_game():
    name = input('\n\nWhats is your name?  ')
    print(f'\nHello {name}!')
    print('----------------------------------------------------------------------------')
    print(f'\n Welcome to HMan {name}, have stored a word for you and\n your job is to gues the word before you hang the poor\n stick person. When prompted, choose a letter that you\n think is in the hidden word. If you are right we will\n give you that letter, but if you are wrong, Hangtime 😈')
    print('----------------------------------------------------------------------------')
    
    
    def ready():
        answer = input("\n\nAre you ready? y/n     ")
        if answer == "y":
            while num_wrong_guesses != 6:
                hide_word(random_word)
                print('----------------------------------------------------------------')
                print(f'\nYour word has {len(hidden_word)} letters, here is your word: \n\n                         {hidden_word}')
                print('----------------------------------------------------------------')
                print(f'THIS SHOULD NOT PRINT: {random_word}')
                letter = input('\n\nWhat is your letter?      ')
                letter_guessed(letter)
                check_status(num_wrong_guesses)
            
        elif answer == 'n':
            pass
    ready()


start_game()

# * Prompt the user to enter a letter.

# * If the letter is in the word, mark it as revealed and visually display that letter in the word.
# * If the letter is incorrect, draw another part onto the stick person.
    