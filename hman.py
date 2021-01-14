import random

# List of words
words = ['audi', 'ferrari', 'bmw', 'porsche', 'toyota']


def hangman(array):
    secret_word = random.choice(array)
    print(secret_word)
    count = len(secret_word)
    hidden_word = ("_" * count)
    print(hidden_word)

    user_inputs = []
    number_of_attempts = 0


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


print(hangman(words))
