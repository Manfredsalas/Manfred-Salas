guess = int (input('chose a number betwen 1 and 10 '))
while True:
    if guess == 3:
        print ('congrants you have the correct answer ')
        break
    elif guess > 10:
        print('your number is to high ')
        guess = int (input('stay in the range 1 to 10 '))
    elif guess < 3:
        print('your number ir to high ')
        guess = int (input(' try again '))
    elif guess > 3:
        print('your number is to low ')
        guess = int (input('try again '))
