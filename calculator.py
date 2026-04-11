# https://github.com/YanellaFT/lab11-HN-YFT
# Partner 1:
# Partner 2: Yanella Fernandez Teusen

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        return b / a
    except:
        raise ZeroDivisionError

def log(a, b):
    try:
        return math.log(b, a)
    except:
        raise ValueError

def exp(a, b):
    return a ** b



