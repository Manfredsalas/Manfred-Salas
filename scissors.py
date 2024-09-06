import random

opcions = ["rock", "paper", "scissors"]


while True:
    user_ch = input('Choose rock, paper or scissors: ')
    computer_ch = random.choice(opcions)

    if user_ch == 'quit':
        break
 
    if user_ch == 'lizard':
        print('Choose rock, paper or scissors')
        continue
    
    if user_ch == computer_ch:
        print("tie") 
    elif (user_ch == "rock" and computer_ch == 'scissors') or (user_ch == "scissors" and computer_ch == "paper") or (user_ch == 'paper' and computer_ch == 'rock' ):
        print('you won!')
    else:
        print('lose')