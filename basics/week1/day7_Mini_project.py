import random

n = random.randrange(0,10)
guessed = False


print("Give a number from 0 to 10")
try:
    guess = int(input())

    while(guessed == False):
        if guess > n:
            print("Lower!")
            guess = int(input())
        elif guess < n:
            print("Higher!")
            guess = int(input())
        else:
            print("Correct!")
            guessed == True 
            break
except ValueError:
    print("Please use a valid number (eg: 1,2,3...)")