
# 10
sum = 0
x = int(input("please enter a number:"))
while x >= 0:
    sum = sum + x
    x = int(input("please enter a number:"))
print(f'sum is {sum}')

# 11
x = int(input("please enter a number for atzeret:"))
atz = 1
for x in range(1, x + 1):
    atz = atz * x
print(f'atzeret = {atz}')

#12
lucky = [3, 17, 23, 39, 41]
backup = lucky.copy()
guess = 0
while len(lucky) > 0:
    num = int(input('Please guess a number [2-49]:'))
    if num < 2 or num > 49:
        continue
    guess = guess + 1
    if guess > 20:
        guess = 0
        lucky = backup.copy()
        continue
    if num in lucky:
        lucky.remove(num)
    elif num in backup:
        print('game over you guessed same numebr twice')
        break
    else:
        print("wrong guess")

if len(lucky) == 0:
    print(f"well done. you did it in {guess}")





