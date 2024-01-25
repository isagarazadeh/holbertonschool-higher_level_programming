#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lsd = number % 10
else:
    lsd = -1 * (-1 * number % 10)
if lsd > 5:
    print(f"Last digit of {number} is {lsd} and is greater than 5")
elif lsd == 0:
    print(f"Last digit of {number} is {lsd} and is 0")
else:
    print(f"Last digit of {number} is {lsd} and is less than 6 and not 0")
