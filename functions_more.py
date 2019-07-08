import random # brings random into my program
print(random.randint(1, 10)) # random number between 1-10

# python core
# print len ....

def print10RandomNumbers(): # between 100-200
    for n in range(10):
        print(random.randint(100, 200))

# default values must be aligned to right
def printRandomNum(howMany = 10, lower = 100,
                   upper = random.randint(1000, 2000)):
    for n in range(howMany):
        print(random.randint(lower, upper))

printRandomNum() # ==> printRandomNum(10, 100, 200)
printRandomNum(2, -5, 30)
printRandomNum(upper = 500)

def profilePrint(age = 18, name = 'incognito'):
    print(f'hello {name} your age is {age}')

# send only name
profilePrint(name = 'John')
profilePrint(name = 'Bob', age = 33)
# send nothing
profilePrint()
# send both parameters
profilePrint(19, 'Dave')
profilePrint()











