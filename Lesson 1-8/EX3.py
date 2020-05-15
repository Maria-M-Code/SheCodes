import random

def chech_guess(num):
    x = int(input("Enter a number from 1-100:\n"))
    if (x == num):
        print ("You won")
    else:
        print("Oh no! You lost!")

def guess_number():
    num = random.randint(1, 100)
    chech_guess(num)


