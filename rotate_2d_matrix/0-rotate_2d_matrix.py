#!/usr/bin/python3
"""Module that rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Rotate 2D Matrix 90 degrees clockwise in place."""

    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
