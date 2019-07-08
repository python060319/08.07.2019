
# guessing game
def printHint(x, guess):
    pass

# create a random number between 1-100
x = 1 # replace this code with random number 1-100
guess = int(input("Guess a number between 1-100:"))
while guess != x:
    printHint(x, guess)
    guess = int(input("Guess a number between 1-100:"))

# create a funciton for the entire game - play
# add a parameter for this function
# which indicates the range of random numbers
# call the game twice playHint
