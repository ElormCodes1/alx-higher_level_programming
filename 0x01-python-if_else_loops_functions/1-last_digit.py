#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
text = "and is less tha 6 and not 0"
if(number < 0):
    lastNumber = int(str(number)[-1]) * -1
else:
    lastNumber = int(str(number)[-1])
if(lastNumber > 5):
    print("Last digit of", number, "is", lastNumber, "and is greater than 5")
elif(lastNumber < 6 and lastNumber != 0):
    print("Last digit of {} is {} and is less than 6 and not 0".format(number,lastNumber))
elif(lastNumber == 0):
    print("Last digit of", number, "is", lastNumber, "and is 0")
