'''
Module: writer.py
Description: This module contains the functions that are used to write data.
'''

from data_toolkit.core.operations import log

def dwrite_data(file_pat, data):
    with open(file_path, 'w') as f:
        f.write(data)
        
    log(f"Dat writtent to {file_path}")
    