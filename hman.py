import random, functools
from stages import man_stages

class Man:
    """ This is a stack class to draw the man  """
    def __init__(self):
        self.stages = man_stages.copy()
        self.current = ''

    def set_stage(self):
        if len(self.stages) == 0: return
        self.current = self.stages.pop()


class Word:
    def __init__(self, word):
        self.word = word
        self.guesses = []
        self.display = ['_ '] * len(word)

    def check_match(self, letter):
        # return 1 or 0 (T/F)
        self.guesses.append(letter)
        matched = 0
        for i in range(len(self.word)):
            # if the letter is a match, mark it in display
            if self.word[i] == letter:
                matched = 1
                self.display[i] = letter
        return matched     
    
    def display_progress(self):
        return functools.reduce(lambda string, char: string+char, self.display)


class HmanGame:
    def __init__(self):
        self.word_bank = ('orzo', 'linguine', 'penne', 'spaghetti', 'linguini', 'rotini')
        self.game_over = False
    
    def verfiy_guess(self, letter):
        """ Validate user input """
        if len(letter) > 1 or len(letter) == 0: return False
        if not letter.isalpha(): return False
        return True

    def start_game(self):
        """ Start the game by choosing a word and setting the stage to the empty man """
        ind = random.randint(0, len(self.word_bank)-1)
        self.word = Word(self.word_bank[ind])
        self.man = Man()
        self.man.set_stage()

    def display_game(self):
        """ Display the current man stage, current word stage and guessed bank """
        print(self.man.current)
        print(f"You have {len(self.man.stages)} guesses left")
        print("You have guessed:", self.word.guesses)
        print("The word you need", self.word.display_progress())

    def check_game_over(self):
        if '_ ' not in self.word.display: return True
        if len(self.man.stages) == 0: return True
        return False

    def play_game(self):
            # 1. display
            self.display_game()
            # 2. get input
            print("What letter would you like to guess?")
            guess = input()
            if not self.verfiy_guess(guess):
                print("\nPLEASE ENTER A LETTER")
                self.play_game()
            # 3. Check for match
            if self.word.check_match(guess.lower()): 
                if self.check_game_over(): 
                    if not self.game_over: print(f"\nGame Over, you win! The word was {self.word.word}.")
                    self.game_over = True
                    return 
                self.play_game()
            # 4. If no match, alter hman state
            if not self.game_over: self.man.set_stage()
            # 5. Take it from the top
            if self.check_game_over(): 
                if not self.game_over:
                    print(self.man.current) 
                    print(f"\nGame Over, you lost. The word was {self.word.word}.")
                self.game_over = True
                return 
            self.play_game()

def run_game(game):
    game.start_game()
    game.play_game()

    if game.game_over: 
        print('Do you want to play again? (Y/N)')
        answer = input()
        if answer.lower() == 'y': 
            new_game = HmanGame()
            run_game(new_game)
        else: 
            return


game = HmanGame()
run_game(game)
print('Goodbye')