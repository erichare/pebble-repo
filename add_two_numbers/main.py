import time
import numpy as np
import os # Test

test = os.environ

print("I'm testing a load print!")

def add_test(firstNumber: float=4, secondNumber: float=5):
    # Compute the add
    print(os.environ)
    time.sleep(1)
    print("Bye")
    print(test)
    time.sleep(1)
    result = firstNumber + secondNumber

    return result

def subtract(firstNumber: float=4, secondNumber: float=5):
    # Compute the add
    result = firstNumber * secondNumber

    return result
