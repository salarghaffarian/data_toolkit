'''
Module: reader.py
Description: This module contains the functions that are used to read data.
'''

from .writer import write_data
from data_toolkit.core.operations import log

def read_data(file_path):
    try:
        with open(file_path, 'r') as f:
            data = f.read()
            log(f"Data read from {file_path}")
            return data

    except FileNotFoundError:
        log(f"File not found: {file_apth}")
        return None