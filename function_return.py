
# function with return value
def getAreaCircle(rad):
    area = 3.14 * rad ** 2
    if area > 0:
        return area # ends the function!!!
    print('the radius was 0 or negative')

def getAreaHekef(rad):
    pass

# null None Empty
#result = getAreaCircle(1.5)
#print(result)

print(f'the area for radius 1.5 is : {getAreaCircle(1.5)}')
len([1,2,3])
