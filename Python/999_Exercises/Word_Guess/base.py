
import random

wordle = []


with open('wordle.txt') as f:
    for line in f:
        l = line.strip()
        wordle.append(l)

f.close()
y = wordle[random.randrange(2315)]
for x in range(0,6):
    x = input("Guess a word")
    if x == f:
        print("correct")
    else:
        print("incorrect")
print (y)
    


