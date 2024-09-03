
#For loop number 1
for hello in range(10):
    print('Hello!')
#For loop number 2
for i in range(15):
    i=i+1
    print('Hello i is set to ' + str(i))
#For loop number 3 and 4 
n = 1000000
sum = n * (n+1)/2
print('The sum is equal to ' + str(sum))

#For loop number 5
integer1 = input('please enter an integer between 1 and 10: ')
integer2 = input('please enter other integer between 1 and 10: ')
integer1 = int(integer1)
integer2 = int(integer2)
for number in range(integer1,integer2, 2):
    print(number**2)
#For loop number 6
integerty = input('please enter an integer: ')
integerty = int(integerty)
if integerty ==2:
    print('prime number')
elif integerty %2 == 0:
    print('even number ')
else:
    print('print number ')
