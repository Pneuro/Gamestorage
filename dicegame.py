import random

dice = random.randint(1, 6)
print(dice)

guess =input("Enter your guess, what did the dice roll")

while int(guess) != int(dice):
    print("Try again")
    guess = input()
    if int(guess) == int(dice):
        break
print("You've quessed correctly")