import random 
print('chose one word (python java javascript ruby html css)') 
word_list = ['python', 'java', 'javascript', 'ruby', 'html', 'css'] 
Chose_word = random.choice(word_list) 
guess = input('chose a word: ') 
while True:
    
    if guess == Chose_word: 
        print('congrantulation you have tha correct word: ') 
        break
    elif guess != Chose_word: 
        print('you dont chose the correct answer: ') 
        guess = input('chose other word: ')