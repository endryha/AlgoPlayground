import copy
from typing import List

from array_utils import print_2d_array

input_matrix = [[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 0, 14, 15],
                [16, 17, 18, 19, 20]]


def zero_striping_hash_sets(matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return

    zero_rows = set()
    zero_columns = set()

    rows = len(input_matrix)
    columns = len(input_matrix[0])

    for i in range(rows):
        for j in range(columns):
            num = matrix[i][j]
            if num == 0 and num not in zero_rows and num not in zero_columns:
                zero_rows.add(i)
                zero_columns.add(j)

    for i in zero_rows:
        for j in range(columns):
            matrix[i][j] = 0

    for j in zero_columns:
        for i in range(rows):
            matrix[i][j] = 0


def zero_striping_in_place(matrix: List[List[int]]) -> None:
    rows = len(input_matrix)
    columns = len(input_matrix[0])

    first_row_has_zero = False
    first_column_has_zero = False

    for i in range(rows):
        if matrix[i][0] == 0:
            first_column_has_zero = True
            break

    for i in range(columns):
        if matrix[0][i] == 0:
            first_row_has_zero = True
            break

    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0

    for i in range(1, rows):
        for j in range(1, columns):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_row_has_zero:
        for i in range(columns):
            matrix[0][i] = 0

    if first_column_has_zero:
        for i in range(rows):
            matrix[i][0] = 0


input_matrix1 = copy.deepcopy(input_matrix)
input_matrix2 = copy.deepcopy(input_matrix)

print_2d_array(input_matrix)

zero_striping_hash_sets(input_matrix1)
print()
print_2d_array(input_matrix1)

zero_striping_in_place(input_matrix2)
print()
print_2d_array(input_matrix2)
