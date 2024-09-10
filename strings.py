print('Write your name: ')
fisrt_name = input()
print('Write your last name: ')
last_name = input()

fisrt_name_len = len(fisrt_name)
last_name_len = len(last_name)
full_name_len = fisrt_name_len + last_name_len

print(f'Hi {last_name} {fisrt_name} your name has {full_name_len} letters. Your initials are {fisrt_name[0]}{last_name[0]}. ')

fisrt_name_backward = fisrt_name[::-1]
double_name = ""
for i in fisrt_name:
    double_name += i * 2

print(f'{double_name}, your name in backward is {fisrt_name_backward}')