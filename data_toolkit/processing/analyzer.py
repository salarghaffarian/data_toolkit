'''
Module: analyzer.py
Description: This module contains the functions that are used to analyze data.
'''

from data_toolkit.core.utils import log
from data_toolkit.processing.transformer import to_uppercase

def word_count(data):
    word_count = len(data.split())
    log(f"Counted {word_count} words")
    return word_count

def count_lines(data):
    line_count = len(data.splitlines())
    log(f"Counted {line_count} lines")
    return line_count
