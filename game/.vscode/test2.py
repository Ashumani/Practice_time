our_number=30
guessed_number = int(input('enter the number between 1 to 60: '))
print ('Types of our number and guessed number is {},{}'.format(type(our_number), type(guessed_number)))
print('Condition is: {}'. format(guessed_number == our_number))
while True:
    print('condition is: {}'. format(guessed_number == our_number))
    if guessed_number == our_number:
        print('congratulation...!! you have entered correct number')
        break
    else:
        print('Try again... dude')
        guessed_number = int(input('enter the number between 1 to 60: '))
        break



        