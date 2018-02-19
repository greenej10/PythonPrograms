number = 7
running = True

while running:
    guess = int(input('guess the lucky number 1 - 10 (positive integers only): '))

    if guess == number:
        print('the guessed number is correct')
        # this causes the while loop to stop
        running = False
    elif guess < number < 11:
        print('please enter a higher number')
    elif guess > number > 0:
        print('please enter a lower number')
else:
    print('This loop is over')

print('control flow program complete')