our_number = 50
user_chance = 5
#print('you have only 5 chance to guess the number')
guessed_number = int(input('Enter your choice between 0 and 100: '))
print('Types of our number and guessed number is {}, {}'.format(type(our_number), type(guessed_number)))
print('Condition is: {}'.format(guessed_number == our_number))

while True:
    print('Condition is: {}'.format(guessed_number == our_number))
    if guessed_number == our_number:
        print('You have guessed correctly')
        break
    else:
        print('Try again. !!!')
        guessed_number = int(input('enter your choice between 0 and 100 :'))
        #user_chance = user_chance - 1
        #print('chance remaining ',user_chance)
        #if user_chance == 0:
            #print('You loss!!!!!')
            #break



exit()

