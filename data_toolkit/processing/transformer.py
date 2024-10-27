'''
Module: transformer.py
Description: This module contains the functions that are used to transform data.
'''

from data_toolkit.core.utils import log

def to_uppercase(data):
    results = data.upper()
    log("Transformed data to uppercase")
    return results

def to_lowercase(data):
    results = data.lower()
    log("Transformed data to lowercase")
    return results