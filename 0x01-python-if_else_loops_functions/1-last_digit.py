#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digit = number % 10
    if last_digit > 5:
        size = "and is greater than 5"
    elif last_digit == 0:
        size = "and is 0"
    else:
        size = "and is less than 6 and not 0"
elif number < 0:
    last_digit = number % -10
    size = "and is less than 6 and not 0"
else:
    last_digit = 0
    size = "and is 0"
print(f"Last digit of {number} is {last_digit} {size}")
