import math
import random

print(math.sqrt(25))
print(math.pi)

print(random.randint(1,10))

def diceroller():
    return str(random.randint(1,6))

print(diceroller())

print("How many dice do you wish to roll?")
amount = int(input())

n = 0

while amount > n:
    print(diceroller())
    n += 1
    