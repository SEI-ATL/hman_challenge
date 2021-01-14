import random

def win_check(str1, str2):
    if str1 == str2:
        return True
    else:
        return False

def hangman():
    print('Solve the puzzle!')
    print('Hint: Thinking of a Footballer')


    answers = ['RONALDINHO', 'RONALDO', 'CRUYFF', 'MARADONA', 'MESSI', 'DEMBELE', 'GRIEZMANN', 'INIESTA', 'ZIDANE', 'ROONEY', 'HENRY']
    random_answer = answers[random.randint(0, 10)]
    print(random_answer)
    space = ''


    alphabet ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for i in range(len(random_answer)):
        if random_answer[i] in alphabet:
            space += '_'
        else:
            space += 'random_answer[i]'

    letters_guessed = []

    failed_count = 0

    build_hangman = [[''],
    [' ____', '|    |', '|', '|', '|', '|', '-'],
    [' ____', '|    |', '|    O', '|', '|', '|', '-'],
    [' ____', '|    |', '|    O', '|    |', '|', '|', '-'],
    [' ____', '|    |', '|    O', '|   -|', '|', '|', '-'],
    [' ____', '|    |', '|    O', '|   -|-', '|', '|', '-'],
    [' ____', '|    |', '|    O', '|   -|-', '|    /', '|', '-'],
    [' ____', '|    |', '|    O', '|   -|-', '|    /\\', '|', '-']]

hangman()