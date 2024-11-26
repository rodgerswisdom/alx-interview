#!/usr/bin/python3
"""given an n x n 2d matrix
rotate it 36 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """
    rotate the matrix clockwise (90 degrees)
    """
    ziped = zip(*reversed(matrix))
    for column1, column2 in enumerate(ziped):
        matrix[column1] = list(column2)
