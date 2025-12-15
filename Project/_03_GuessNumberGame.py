# random.randint() -> generating random no.
# int(input()) -> take an int from user
# while -> to continue until user guesses the no.
# guess_count -> to count the no. of guesses to win

import random
randint = random.randint(1,10)
guess_count = 1
guess = int(input('Guess a number between 1 and 10: '))
while randint != guess:
    guess_count +=1
    if guess > randint:
        print('greater than no.')
    else:
        print('smaller than no.')
    guess = int(input('Guess again: '))
print(f'You guessed in {guess_count} times, the number was {guess}.')
