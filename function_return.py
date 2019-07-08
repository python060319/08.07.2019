import math

# function with return value
def getAreaCircle(rad):
    area = math.pi * rad ** 2
    if area > 0:
        return area # ends the function!!!
    print('the radius was 0 or negative')

def getAreaHekef(rad):
    return math.pi * 2 * rad

# null None Empty
#result = getAreaCircle(1.5)
#print(result)

print(f'the area for radius 1.5 is : {getAreaCircle(1.5)}')

l1 = [ getAreaHekef(3.5), getAreaCircle(7.9) ]
