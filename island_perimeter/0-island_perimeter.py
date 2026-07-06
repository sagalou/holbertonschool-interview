#!/usr/bin/python3
"""Module that returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """Return the perimeter of the island described in grid.

    Args:
        grid (list): list of lists of integers, where 0 is water
            and 1 is land.

    Returns:
        int: perimeter of the island.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
