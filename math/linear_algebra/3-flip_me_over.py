#!/usr/bin/env python3


def matrix_transpose(matrix):
    """Returns the transpose of the matrix."""
    return [list(row) for row in zip(*matrix)]
