
import random

def guess(x):
    random_number = random.randint(1,x)
    guess =0
    while guess != random_number:
        guess =  int(input(f"Guess a number between 1 and {x}: " ))
        if guess < random_number:
            print(" guess no is to low")
        elif guess > random_number:
            print("guess no is too high")

    print(f"Congo you have guessed the number!!! {random_number}")  
        

def comp_guess(x):
    low=1
    high = x
    feedback = " "
    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess= low 
        feedback = input(f"is {guess} too high (H), too low (L), or correct (C)??").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low= guess + 1
    print(f"congo you guess number , {guess}!!")

comp_guess(10)









    





