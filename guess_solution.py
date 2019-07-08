import random

def printHint(realNumber, ourGuess):
    if realNumber > ourGuess:
        print('guess higher...')
    else:
        print('guess lower...')

def playGame(min = 1, max = 100):
    # create a random number between 1-100
    x = random.randint(min, max)
    guess = int(input(f"Guess a number between {min}-{max}:"))
    while guess != x:
        printHint(x, guess)
        guess = int(input(f"Guess a number between {min}-{max}:"))
    print(f'correct ... the number: {guess}')

playGame(1, 10)
playGame(2, 30)
