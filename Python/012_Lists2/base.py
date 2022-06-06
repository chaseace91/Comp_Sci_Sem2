import random
y = int(input("How many random numbers do you want"))
number = []
for i in range(y):
    number.append(random.randrange(10))
y = 0
for i in number:
    print(i, end=", ")
    y=y+1
    print()
    