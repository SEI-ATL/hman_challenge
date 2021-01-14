
import random

word_bank = ['apple', 'anime', 'impeachment', 'coding', 'computer', 'automation', 'library' ]

chosen_word = random.choice(word_bank)




all_body="""  
  ||||||||||||||||
  ||         |   
  ||         |
  ||         -       
  ||      >(* *)<
  ||        |^|
  ||   >---& \/ &---<
  ||         ||
  ||        #  #
  ||        &  &      
  ||           
              """

no_legs="""  
  ||||||||||||||||
  ||         |   
  ||         |
  ||         -       
  ||      >(* *)<
  ||        |^|
  ||   >---& \/ &---<
  ||         ||
  ||          
  ||              
  ||           
              """
no_arms="""  
  ||||||||||||||||
  ||         |   
  ||         |
  ||         -       
  ||      >(* *)<
  ||        |^|
  ||       & \/ &
  ||         ||
  ||          
  ||              
  ||               """

head="""  
  ||||||||||||||||
  ||         |   
  ||         |
  ||         -       
  ||      >(* *)<
  ||        |^|
  ||       
  ||        
  ||          
  ||              
  ||               """
pole ="""  
  ||||||||||||||||
  ||         |   
  ||         |
  ||             
  ||      
  ||        
  ||       
  ||        
  ||          
  ||              
  ||               """

image = {
    1 : pole,
    2 : head,
    3 : no_arms,
    4 : no_legs,
    5 : all_body

}

def hangman(arr):
    chosen_word = random.choice(arr)
    display_word =('_' * len(chosen_word))
    print(display_word)
    # print(chosen_word)
    gameword = list(chosen_word)
    user_win = 0
    computer_win = 0
    word_so_far=""
    a=0 
    while user_win != len(gameword)+a or computer_win != 5:
        
        
        for i in range(len(gameword)):
            left_to_guess=chosen_word[len(word_so_far):]
            # print(f"left to guess {left_to_guess}")
            letter=input('Please Enter Your Letter: ')
            if letter == left_to_guess:
                print("You win!")
                print(chosen_word)
                hangman(arr) 
            while len(letter)>1:
                letter=input('Please enter a single character: ')
            if letter == gameword[i-a]:
                user_win = user_win + 1
                num =len(gameword)-user_win
                display_word = word_so_far+letter+('_'* num)
                word_so_far=word_so_far+letter
                # print(user_win)
                # print(word_so_far)
                print(display_word)
                if user_win == len(gameword):
                    chosen_word = random.choice(arr) 
                    print(chosen_word) 
                    print('You Win!')
                    hangman(arr) 
                    
            else:  
                
                num =len(gameword)-i
                display_word = word_so_far+('_'* num)
                print(display_word)
                computer_win = computer_win + 1
                print(image[computer_win])
                a=a+1
                if computer_win==5:
                   print(chosen_word) 
                   print('Computer Wins')
                   hangman(arr)
hangman(word_bank)
        