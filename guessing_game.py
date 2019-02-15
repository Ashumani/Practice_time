#! bin/env/python

# import random for generating random number
import random

# generate random number using random.random int in range 0 to 100
random_number = random.randint(0, 100)


# print('Random number', random_number)
# get total number of chances
chances = 5

print('*'*10, 'Welcome to guessing game', '*'*10)


while chances >= 1:  # works only till chances greater than 0
    guess_number = int(input('Enter a number: '))
    if guess_number == random_number:
        break
    else:
        print('YOu guess was wrong. Try again !!')
        print('YOu are left with {} chances.'.format((chances - 1)))
        chances -= 1

if chances == 0:
    print('Game Over !!!')
    print('Do you wanna play again (Y/n): ')
else:
    print('YAA !! YOu won the game')

