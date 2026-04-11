# https://github.com/YanellaFT/lab11-HN-YFT
# Partner 1: Hai Nguyen
# Partner 2: Yanella Fernandez Teusen

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math
# First example

def square_root(a):
    try:
        answer = math.sqrt(a)
    except:
        raise ValueError
    return answer

def hypotenuse(a,b):
    return math.hypot(a,b)

def add(a, b): 
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    try:
        answer = b/a
    except:
        raise ZeroDivisionError

    return answer

def logarithm(a,b):
    try:
        answer = math.log(b,a)
    except:
        raise ValueError
    return answer

def exponent(a,b):
    return a**b





