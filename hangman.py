import random

misses = 0
words = ['python', 'javascript', 'pizza', 'vscode', 'seltzer', 'bowser']
previous_guesses = []
game_won = False

def init(first_time):
    global previous_guesses, misses
    if first_time:
        print("Welcome to hangman! Do you want to play?")
        play_or_nah = input("y/n: ")
        if play_or_nah.lower() == 'y':
            game_loop()
        else:
            print("All good. See ya later!")
            return
    else:
        previous_guesses = []
        misses = 0
        game_loop()

def game_loop():
    secret_word = words[random.randrange(0, len(words))]
    while misses < 6:
        print("\n---------------------")
        print(secret_word)
        print(f'You have {misses}/6 misses')
        print(f'Previous guesses: {previous_guesses}')
        print(f'The word you are looking for: {format_secret(secret_word, previous_guesses)}')
        print(handle_guess(secret_word))
        check_win(previous_guesses, secret_word)
        if game_won:
            print('--------------------------------------------')
            break
    game_over(False, secret_word)


def format_secret(str, guesses):
    secret_list = list(str)
    for i in range(len(secret_list)):
        if secret_list[i] not in guesses:
            secret_list[i] = "_"
    return " ".join(secret_list)

def handle_guess(word):
    guess = input('Guess a letter! --> ')
    while guess not in 'qwertyuiopasdfghjklzxcvbnm' or len(guess) != 1:
        guess = input('\tInvalid input, try again! --> ')
    previous_guesses.append(guess.lower())
    if guess in list(word):
        return "Correct!"
    else:
        global misses
        misses += 1
        return "Incorrect."

def game_over(win, word):
    if win:
        print(f'You did it! The word was {word}')
    else: 
        print(f'Game Over. The word was {word}')
    play_again = input('Play again? y/n --> ')
    if play_again.lower() == 'y':
        init(False)
    else:
        print("All good. See ya later!")


def check_win(guesses, word):
    global game_won
    correct_letters_needed = len(word)
    correct_guessed = 0
    for i in word:
        if i in guesses:
            correct_guessed += 1
    if correct_guessed == correct_letters_needed:
        game_won = True
        game_over(True, word)
    else:
        return
        


        

# print(format_secret("hello", ['h', 'o', 'y', 'j']))
init(True)
