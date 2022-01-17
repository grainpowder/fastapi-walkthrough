from fastwalk.models.algebra import *
import numpy as np


def is_row_count_valid(matrix: Matrix):
    return matrix.row_count == len(matrix.values)


def are_columns_valid(matrix: Matrix):
    for row in matrix.values:
        is_col_count_invalid = len(row) != matrix.col_count
        is_element_null = any([element is None for element in row])
        if is_col_count_invalid or is_element_null:
            return False
    return True


def is_matrix_valid(matrix: Matrix):
    return is_row_count_valid(matrix) and are_columns_valid(matrix)


def calculate_determinant(matrix: Matrix) -> float:
    matrix_array = np.array(matrix.values)
    return np.linalg.det(matrix_array)
