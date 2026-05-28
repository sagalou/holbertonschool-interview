#!/usr/bin/python3
"""Module that calcultes the fewest number of operations needed
to result in a given characters"""


def minOperations(n):
    """Determines the mininum of operations to calculte a given number"""
    operation = 0
    while n > 1:
        for p in range(2, n + 1):
            if n % p == 0:
                operation += p
                n = n // p
                break
    return operation
