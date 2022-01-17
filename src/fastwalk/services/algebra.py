from fastwalk.models.algebra import *
import numpy as np


def is_row_count_valid(matrix: Matrix):
    return matrix.row_count == len(matrix.values)


def are_columns_valid(matrix: Matrix):
    for row in matrix.values:
        if len(row) != matrix.col_count:
            return False
    return True


def calculate_determinant(matrix: Matrix) -> float:
    matrix_array = np.array(matrix.values)
    return np.linalg.det(matrix_array)
