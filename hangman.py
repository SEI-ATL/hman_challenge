import random

bank = ['chonners', 'starships', 'mayonnaise', 'recursion', 'america']
random_word = random.choice(bank)

feet = """ 
__________________
|        |
|        | 
|     ( 0 0 )
|        -
|    --- | ----
|        |
|       / |
|    __/  |__
|               """

legs = """ 
__________________
|        |
|        | 
|     ( 0 0 )
|        -
|    --- | ----
|        |
|       / |
|      /  |
|               """

arms = """ 
__________________
|        |
|        | 
|     ( 0 0 )
|        -
|    --- | ----
|        |
|
|
|               """

body = """ 
__________________
|        |
|        | 
|     ( 0 0 )
|        -
|        |
|        |
|
|
|               """

head = """ 
__________________
|        |
|        | 
|     ( 0 0 )
|        -
|
|
|
|
|               """

noose = """ 
__________________
|        |
|        | 
|
|
|
|
|
|
|               """


hangman_build = {
    1: noose,
    2: head,
    3: body,
    4: arms,
    5: legs,
    6: feet
}

def hangman(arr):
    random_word = random.choice(arr)
    hidden_word = ('_' * len(random_word))
    print(hidden_word)
    word = list(random_word)
    word_so_far = ''

    tries = 6
    user_points = 0
    computer_points = 0

    while tries > 0 or user_points != len(word):
        for i in range(len(word)):
            guess = input('Enter your guess\n')
            if guess == word[i]:
                user_points = user_points + 1
                hidden_word = word_so_far + guess + ('_' * len(word) - user_points)
                print(word_so_far)
                if user_points == len(word):
                    print('User wins')
            else:
                computer_points = computer_points + 1
                print(hangman_build[computer_points])
                if computer_points == 6:
                    print('Computer wins')

hangman(bank)