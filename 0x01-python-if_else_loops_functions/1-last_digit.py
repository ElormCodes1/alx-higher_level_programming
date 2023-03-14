#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastNumber1 = str(number)[-1]
lastNumber2 = int(lastNumber1)
if lastNumber2 > 5:
    print("Last digit of", number, "is", lastNumber1, "and is greater than 5")
elif lastNumber2 < 6 and lastNumber2 != 0:
    print("Last digit of", number, "is", lastNumber1, "and is less than 6 and not 0")
elif lastNumber2 == 0:
    print("Last digit of", number, "is", lastNumber1, "and is 0")
