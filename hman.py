import random

word_list = ['apple', 'banana', 'orange', 'watermelon',
             'mango', 'peach', 'pineapple', 'kiwi']


def random_word(arr):
    random_num = random.randint(0, len(arr) - 1)
    return arr[random_num]


# secret_word = random_word(word_list)
secret_word = 'banana'
dashed_word = ''
guesses_left = 3
game_over = False


def run_game():
    global dashed_word
    print(secret_word)
    for letter in secret_word:
        dashed_word += '– '
    print('Let\'s play H-Man! Here\'s your word:')
    print(dashed_word)
    print('What letter would you like to guess? ')
    while game_over == False:
        handle_input()
    return


def handle_input():
    global dashed_word
    guess = input()
    if guess in secret_word:
        i = 0
        for letter in secret_word:
            if letter == guess:
                idx = secret_word.index(letter, i, i + 1) * 2
                dashed_word = dashed_word[:idx] + \
                    letter + dashed_word[idx + 1:]
            i += 1
        print(dashed_word)
        handle_win()
    else:
        handle_loss()


def handle_win():
    global game_over
    if '–' in dashed_word:
        print('Good guess! Guess a different letter. ')
    else:
        print('You win!')
        game_over = True


def handle_loss():
    global game_over
    global guesses_left
    if guesses_left >= 1:
        guesses_left -= 1
        print(
            f'Nope. You have {guesses_left} guesses left. Guess a different letter. ')
    else:
        print('Oh no! You ran out of guesses. I\'m afraid this is the end.')
        game_over = True


run_game()
