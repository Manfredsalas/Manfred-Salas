import random
def result(text):
    print(f'**********{text}**********')

def pepe():
    options = [ '1', '2', '3']
    comp_options = ['1', '2', '3']

    while True:
        result('Choose rock(1), paper(2) or scissors(3): ')
        user_ch = input()
        computer_ch = random.choice(comp_options)
        print(computer_ch)

        if user_ch == 'quit':
            break
 
        if user_ch not in (options):
            result('Choose rock(1), paper(2) or scissors(3): ')
            continue
    
        if user_ch == computer_ch:
            result("tie") 
        elif ((user_ch == '1') and (computer_ch == '3' )) or ((user_ch == '3') and (computer_ch ==  '2' )) or ((user_ch == '2') and (computer_ch == '1' )):
            result('You won!')
        else:
            result('You lose')
pepe()