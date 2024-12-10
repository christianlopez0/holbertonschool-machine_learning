#!/usr/bin/env python3

def matrix_shape(matrix):
    if isinstance(matrix, list):
        return [len(matrix)] + matrix_shape(matrix[0]) if isinstance(matrix[0], list) else [len(matrix)]
    return []
