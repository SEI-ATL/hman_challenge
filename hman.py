import random

# List of words
words = ['audi', 'ferrari', 'bmw', 'porsche', 'toyota']


# def hangman(array):
#     secret_word = random.choice(array)
#     print(secret_word)
#     count = len(secret_word)
#     hidden_word = ("_" * count)
#     print(hidden_word)

#     user_inputs = []
#     number_of_attempts = 0

guesses_left = 6
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

# Rome's solution


def game_init():
    global secret_word
    global letters_left
    global guesses_left
    global letters_guessed
    global errors
    global uncensored_secret_word

    random_index = floor(random() * 6)
    secret_word = words[random_index]
    letters_left = len(secret_word)
    guesses_left = 6

    i = 0
    while i < len(secret_word):
        uncensored_secret_word = uncensored_secret_word + "_ "
        i += 0


def win():
    print('You win')
    print(f"The word was {secret_word}")


def lose():
    print('You lose')


def add_to_guesses(guess):
    letters_guessed.append(guess)


def success(guess):
    global underscored_secret_word
    global win
    print("correct")
    add_to_guesses(guess)
    index = 0
    for letter in secret_word:
        if letter == guess:
            if index == 0
            underscored_secret_word = guess + underscored_secret_word[1:]
        elif index < (len(secret_word) - 1):
            underscored_secret_word = underscored_secret_word[0: (
                index * 2 + 2)] + guess + " "
        else:
            underscored_secret_word = underscored_secret_word[:-2] + guess
    index += 1
    for letter in underscored_secret_word:
        if letter == "_":
            continue_game()
            return
    win()


def hangman(incorrect_guesses_left):
    print(hangman_table[incorrect_guesses_left])


def failure(guess):
    global guesses_left
    add_to_guesses(guess)
    guesses_left -= 1
    print_hangman(guesses_left)
    continue_game()


def already_guessed():
    print('You already guessed that letter')
    continue_game()


def continue_game():
    global errors
    print(f'You have {guesses_left} guesses left.')
    print(f'You have guessed: {letters_guessed}')
    print(f"The word you need: {underscored_secret_word}")
    if guesses_left > 0:
        guess = input('What letter would you like to guess? ').lower()
        if guess == secret_word:
            win()
            return

        for letter in secret_word:
            if letter == guess:
                success(guess)
                return
        failure()
        return
    else:
        lose()


looping = True
game_init()
continue_game()

while looping:
    should_continue = input(
        "Would you like to play again? (Yes or No) ").lower()
    if should_continue == "yes" or should_continue == "y":
        game_init()
        continue_game()
    elif should_continue == "no" or "n":
        print("Thanks for playing.")
        looping = False
