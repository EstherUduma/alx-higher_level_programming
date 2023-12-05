#!/usr/bin/python3
"""
Writes a string to a text file (UTF-8)
and returns a number of characters
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8)
    and returns a number of characters
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        return file.write(text)
