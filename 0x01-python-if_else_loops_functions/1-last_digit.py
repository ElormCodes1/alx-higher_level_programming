#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if(number < 0):
    lastNumber = int(str(number)[-1]) * -1
else:
    lastNumber = int(str(number)[-1]
if(lastNumber > 5):
    print("Last digit of", number, "is", lastNumber, "and is greater than 5")
elif(lastNumber < 6 and lastNumber != 0):
    print("Last digit of", number, "is", lastNumber, "and is less than 6 and not 0")
elif(lastNumber == 0):
    print("Last digit of", number, "is", lastNumber, "and is 0")
