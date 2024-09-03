import random

my_number = random.randint(1, 10)
print('Choose a number between 1 and 10 (or write "quit" to stop the game): ')
while True:
    user = input('chose a number ')
    
    if user == 'quit':
        print('You chose to stop the game see you next time :>')
        break
    guess = int(user)
        
    if guess == my_number:
         print('Congrats! You have the correct answer: ')
    elif guess > my_number:
        print('stay in the range 1 to 10 ')
    elif guess > my_number:
        print('Your number is too high. Try again: ')
    elif guess < my_number:
         print('Your number is too low. Try again: ')
