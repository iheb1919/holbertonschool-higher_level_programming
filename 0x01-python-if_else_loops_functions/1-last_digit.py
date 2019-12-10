#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    x = number % -10
else:
    x = number % 10
stupidmessage = " Last digit of {} is {} ".format(number, x)
if x > 5:
    print("{} and is greater than 5".format(stupidmessage))
elif x < 6 and x != 0:
    print("{} and is less than 6 and not 0".format(stupidmessage))
else:
    print("{} and is 0".format(stupidmessage))
