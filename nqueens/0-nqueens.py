#!/usr/bin/python3
"""Module that solves the N queens problem"""


import sys


def queens(n):
    """Placeholder for N queens solution logic."""
    solutions = []

    def backtrack(col, placed):
        if col == n:
            # convert to required format [[r, c], ...]
            solution = [[r, c] for c, r in enumerate(placed)]
            solutions.append(solution)
            return
        for row in range(n):
            if is_safe(placed, row):
                placed.append(row)
                backtrack(col + 1, placed)
                placed.pop()

    backtrack(0, [])
    for sol in solutions:
        print(sol)


def is_safe(placed, row):
    """Return True if placing a queen at given row is safe for next column."""
    col = len(placed)
    for c, r in enumerate(placed):
        # same row
        if r == row:
            return False
        # diagonal
        if abs(r - row) == abs(c - col):
            return False
    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    queens(n)
