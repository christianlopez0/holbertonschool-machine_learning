#!/usr/bin/env python3


def mat_mul(mat1, mat2):
    """Multiplies two matrices and returns the resulting matrix."""
    # Check if the matrices can be multiplied
    if len(mat1[0]) != len(mat2):
        return None

    # Initialize the result matrix with zeros
    result = [[0] * len(mat2[0]) for _ in range(len(mat1))]

    # Perform matrix multiplication
    for i in range(len(mat1)):  # Iterate over rows of mat1
        for j in range(len(mat2[0])):  # Iterate over columns of mat2
            result[i][j] = sum(mat1[i][k] * mat2[k][j] for k in range(len(mat2)))

    return result
