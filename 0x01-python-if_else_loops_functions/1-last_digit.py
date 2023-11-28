#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

def last_digit(num):
    last_digit_unsigned = abs(num) % 10
    return -last_digit_unsigned if (num < 0) else last_digit_unsigned

last_digit = last_digit(number)

if last_digit > 5:
    end_str = "and is greater than 5\n"
elif last_digit == 0:
    end_str = "and is 0\n"
elif last_digit < 6 and last_digit != 0:
    end_str = "and is less than 6 and not 0\n"

print(f"Last digit of {number} is {last_digit} {end_str}")
