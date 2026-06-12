#!/usr/bin/python3
"""Module that deals with UTF-8 Validation"""


def validUTF8(data):
    """Checks if a given data set represents a valid UTF-8 encoding
    Args:
        data (list): A list of integers representing the data set
    Returns:
        bool: True if the data set represents a valid UTF-8 encoding,
        False otherwise
    """
    i = 0
    while i < len(data):
        byte = data[i] & 0xFF
        if byte >> 7 == 0:
            i += 1
        elif byte >> 5 == 0b110:
            if i + 1 >= len(data) or data[i + 1] >> 6 != 0b10:
                return False
            i += 2
        elif byte >> 4 == 0b1110:
            valid = (
                i + 2 < len(data) and
                data[i + 1] >> 6 == 0b10 and
                data[i + 2] >> 6 == 0b10
            )
            if not valid:
                return False
            i += 3
        elif byte >> 3 == 0b11110:
            valid = (
                i + 3 < len(data) and
                data[i + 1] >> 6 == 0b10 and
                data[i + 2] >> 6 == 0b10 and
                data[i + 3] >> 6 == 0b10
            )
            if not valid:
                return False
            i += 4
        else:
            return False
    return True
