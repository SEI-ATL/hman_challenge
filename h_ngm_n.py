import random

def check_win(string1, string2):
    if string1 == string2:
        return True
    else:
        return False

def win_message():
    print('=D')
    print('Congratulations! You have completed the word puzzle. You are now free.')
    revive = input('Continue? (y/n)')
    replay(revive)

def loss_message(mystery_word):
    print('\n')
    print('The correct word was ', mystery_word)
    print('\n')
    print('=O')
    print('You have used all your guesses and have been hanged! Run again to have another chance at life.')
    revive = input('Continue? (y/n)')
    replay(revive)
    
def replay(revive):
    if revive == 'y':
        failed_guess_count = 0
        hangman()

def print_build(count):
    
    build = [[''],
    [' ____', '|    |', '|', '|', '|', '|', '|_______'],
    [' ____', '|    |', '|    O', '|', '|', '|', '|_______'],
    [' ____', '|    |', '|    O', '|    |', '|', '|', '|_______'],
    [' ____', '|    |', '|    O', '|   -|', '|', '|', '|_______'],
    [' ____', '|    |', '|    O', '|   -|-', '|', '|', '|_______'],
    [' ____', '|    |', '|    O', '|   -|-', '|    /', '|', '|_______'],
    [' ____', '|    |', '|    O', '|   -|-', '|    /\\', '|', '|_______']]

    for part in build[count]:
        print(part)


def hangman():

    print('\n')
    print('WELCOME TO JAPANESE HANGMAN!!!')
    print('WHERE YOU ARE A CRIMINAL ABOUT TO BE HANGED')
    print('SOLVE THE PUZZLE TO BE FREED')

    words = ['SHINRINYOKU', 'KOMOREBI', 'KUIDAORE', 'TSUNDOKU', 'WABI-SABI', 'KINTSUGI', 'MONO NO AWARE', 'IRUSU', 'KAROSHI', 'SHOGANAI', 'NATSUKASHII']
    mystery_word = words[random.randint(0, 10)]
    dashes = ''

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in range(len(mystery_word)):
        if mystery_word[i] in alphabet:
            dashes += '_'
        else:
            dashes += mystery_word[i]

    letters_guessed = []
    failed_guess_count = 0

    while failed_guess_count < 7:
        
        print('\n')
        print_build(failed_guess_count)
        print('\n')
        print(dashes)
        print('\n')

        if check_win(dashes, mystery_word):
            win_message()
            break
            
        
        print(f'You have ', 7 - failed_guess_count, ' guesses remaining')
        print('Letters guessed: ', letters_guessed)

        guess = input('Guess a letter: ').upper()

        if len(guess) > 1 or guess not in alphabet:

            guess = input('GUESS A LETTER: ').upper()
            print('Thank you! =D')
            print('\n')

        elif guess in mystery_word:
            for i in range(len(mystery_word)):
                if mystery_word[i] == guess:
                    letters = list(dashes)
                    letters[i] = mystery_word[i]
                    dashes = ''.join(letters)

        else: 
            if guess in letters_guessed:
                print('\n')
                print('You have guessed this letter already. Try another letter.')
            else:
                letters_guessed.append(guess)
                print('Your guess was incorrect.')
                print('\n')
                failed_guess_count += 1

    if failed_guess_count == 7:
        loss_message(mystery_word)

hangman()
