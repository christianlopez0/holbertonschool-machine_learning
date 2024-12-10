#!/usr/bin/env python3


def cat_matrices2D(mat1, mat2, axis=0):
    """Concatenates two 2D matrices along the specified axis."""
    if axis == 0:
        # Concatenate along rows, check if number of columns match
        if len(mat1[0]) != len(mat2[0]):
            return None
        return mat1 + mat2
    elif axis == 1:
        # Concatenate along columns, check if number of rows match
        if len(mat1) != len(mat2):
            return None
        return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    else:
        return None
