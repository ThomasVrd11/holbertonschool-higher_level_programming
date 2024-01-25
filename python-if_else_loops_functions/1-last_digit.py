#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdi = abs(number) % 10
if number < 0:
    lastdi = -lastdi
if (lastdi > 5):
    print(f"Last digit of {number} is {lastdi} and is greater than 5")
elif (lastdi == 0):
    print(f"Last digit of {number} is {lastdi} and is 0")
elif (lastdi < 6):
    print(
        f"Last digit of {number} is {lastdi} and is less than 6 and not 0")
