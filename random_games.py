import random
random_int = random.randint(1, 100)
print(random_int)
user_input=input('enter the number')
while True:
    user_input=int(user_input)
    if user_input > random_int:
        print('the number is given by user is greater ')
    if user_input < random_int:
        print('the number is given by user is smaller')
    if user_input == random_int:
        print('yeh!!! You Won')
        user_input=input('Do you wann to play again [y]/[n]:')
        user_input=int(user_input)
    if user_input =='n' or user_input =='N':
        break
    else:
        random_int = random.randint(1, 100)
        print(random_int)
exit()

