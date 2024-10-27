
'''
Module: operations.py 
Description: This module contains the basic arithmetic operations that can be performed on two numbers.

'''

from .utils import log

def add(a, b):
    results = a + b
    log(f"Adding {a} adn {b} results in {results}")
    return results

def multiply(a, b):
    results = a * b
    log(f"Multiplying {a} and {b} results in {results}")
    return results

def subtract(a, b):
    results = a - b
    log(f"Subtracting {a} and {b} results in {results}")
    return results

def divide(a, b):
    results = a / b
    log(f"Dividing {a} and {b} results in {results}")
    return results
