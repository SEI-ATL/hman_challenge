import random
words = ['dog', 'tree', 'house', 'apple', 'car',
         'python', 'computer', 'desk', 'plant', 'water']


def random_word():
    word = random.choice(words)
    return word.lower()


def game(word):
    underscores = '_' * len(word)
    correct_guess = False
    guessed_letters = []
    guessed_words = []
    attempts = 7
    print('Play the game of Hangman!')
    print('You have ', attempts, 'guesses!')
    print(underscores)
    while not correct_guess and attempts > 0:
        guess = input('Guess a letter or the whole word here: ').lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You already guessed the letter ', guess)
            elif guess not in word:
                print(guess, ' is not the correct word')
                print('You have ', attempts, ' left')
                attempts -= 1
                guessed_letters.append(guess)
            else:
                print(guess, ' is the correct word!')
                guessed_letters.append(guess)
                word_list = list(underscores)
                indexes = [i for i, letter in enumerate(
                    word) if letter == guess]
                for index in indexes:
                    word_list[index] = guess
                complete_word = ''.join(underscores)
                if '_' not in complete_word:
                    correct_guess = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('You already guessed that word')
            elif guess != word:
                print('Not the correct word')
                attempts -= 1
                guessed_words.append(guess)
            else:
                correct_guess = True
                complete_word = word
        else:
            print('Please only guess letters or words')
    if correct_guess == True:
        print('You gueessed the correct word!')
    else:
        print('You ran out of guesses, the correct word was ', word)


def play_game():
    word = random_word()
    game(word)


play_game()
