"""
Unit tests for the Sudoku board verifier.
"""

import unittest
from typing import List

# Assuming print_2d_array is defined in array_utils

# Test boards used for verification
valid_sudoku_board = [
    [3, -1, 6, -1, 5, 8, 4, -1, -1],
    [5, 2, -1, -1, -1, -1, -1, -1, -1],
    [-1, 8, 7, -1, -1, -1, -1, 3, 1],
    [1, -1, 4, 5, -1, -1, 3, 2, -1],
    [9, -1, -1, 8, 6, 3, -1, -1, 5],
    [-1, 5, -1, -1, 9, -1, 6, -1, -1],
    [-1, 3, -1, -1, -1, 7, 2, 5, -1],
    [-1, 1, -1, -1, -1, -1, -1, 7, 4],
    [-1, -1, 5, 2, -1, 6, -1, -1, -1]
]

row_duplicate_sudoku_board = [
    [3, -1, 6, -1, 5, 8, 4, -1, -1],
    [5, 2, -1, -1, -1, -1, -1, -1, -1],
    [-1, 8, 7, -1, -1, -1, -1, 3, 1],
    [1, -1, 2, 5, -1, -1, 3, 2, -1],  # Duplicate '2' in this row (if intended)
    [9, -1, -1, 8, 6, 3, -1, -1, 5],
    [-1, 5, -1, -1, 9, -1, 6, -1, -1],
    [-1, 3, -1, -1, -1, 8, 2, 5, -1],
    [-1, 1, -1, -1, -1, -1, -1, 7, 4],
    [-1, -1, 5, 2, -1, 6, -1, -1, -1]
]

column_duplicate_sudoku_board = [
    [3, -1, 6, -1, 5, 8, 4, 7, -1],  # Duplicate '7' in 8th column (if intended)
    [5, 2, -1, -1, -1, -1, -1, -1, -1],
    [-1, 8, 7, -1, -1, -1, -1, 3, 1],
    [1, -1, 4, 5, -1, -1, 3, 2, -1],
    [9, -1, -1, 8, 6, 3, -1, -1, 5],
    [-1, 5, -1, -1, 9, -1, 6, -1, -1],
    [-1, 3, -1, -1, -1, 7, 2, 5, -1],
    [-1, 1, -1, -1, -1, -1, -1, 7, 4],
    [-1, -1, 5, 2, -1, 6, -1, -1, -1]
]

subgrid_duplicate_sudoku_board = [
    [3, -1, 6, -1, 5, 8, 4, -1, -1],
    [5, 2, -1, -1, -1, -1, -1, -1, -1],
    [-1, 8, 7, -1, -1, -1, -1, 3, 1],
    [1, -1, 4, 5, -1, -1, 3, 2, -1],
    [9, -1, -1, 8, 6, 3, -1, -1, 5],
    [-1, 5, -1, -1, 9, -1, 6, -1, -1],
    [-1, 3, -1, -1, -1, 7, 2, 5, -1],
    [-1, 1, -1, -1, -1, -1, -1, 7, 4],
    [-1, 3, 5, 2, -1, 6, -1, -1, -1]  # Duplicate in one of the subgrids (if intended)
]


def verify_sudoku_board(board: List[List[int]]) -> bool:
    """
    Verify that the given sudoku board does not contain duplicates in any row,
    column, or 3x3 subgrid. -1 is assumed to represent an empty cell.
    """
    rows = len(board)
    columns = len(board[0])

    rows_sets = [set() for _ in range(rows)]
    columns_sets = [set() for _ in range(columns)]
    subgrid_sets = [set() for _ in range(rows)]  # Assuming a 9x9 board => 9 subgrids.

    for i in range(rows):
        for j in range(columns):
            num = board[i][j]

            if num == -1:
                continue

            if num in rows_sets[i]:
                # Detailed messages could be logged instead of printed.
                print(f"Row {i} check failed: {num} ({i},{j})")
                return False

            if num in columns_sets[j]:
                print(f"Column {j} check failed: {num} ({i},{j})")
                return False

            subgrid_idx = (i // 3) * 3 + (j // 3)
            if num in subgrid_sets[subgrid_idx]:
                print(f"Subgrid {subgrid_idx} check failed: {num} ({i},{j})")
                return False

            rows_sets[i].add(num)
            columns_sets[j].add(num)
            subgrid_sets[subgrid_idx].add(num)

    return True


class TestSudokuVerifier(unittest.TestCase):
    def test_valid_sudoku_board(self):
        # Optionally, uncomment for debug:
        # print("Valid Sudoku Board")
        # print_2d_array(valid_sudoku_board)
        result = verify_sudoku_board(valid_sudoku_board)
        self.assertTrue(result, "The valid sudoku board should pass verification.")

    def test_sudoku_board_with_row_duplicate(self):
        # Uncomment if you wish to see the board output:
        # print("Sudoku Board with Row Duplicate:")
        # print_2d_array(row_duplicate_sudoku_board)
        result = verify_sudoku_board(row_duplicate_sudoku_board)
        self.assertFalse(result, "The sudoku board with a row duplicate should fail verification.")

    def test_sudoku_board_with_column_duplicate(self):
        # print("Sudoku Board with Column Duplicate:")
        # print_2d_array(column_duplicate_sudoku_board)
        result = verify_sudoku_board(column_duplicate_sudoku_board)
        self.assertFalse(result, "The sudoku board with a column duplicate should fail verification.")

    def test_sudoku_board_with_subgrid_duplicate(self):
        # print("Sudoku Board with Subgrid Duplicate:")
        # print_2d_array(subgrid_duplicate_sudoku_board)
        result = verify_sudoku_board(subgrid_duplicate_sudoku_board)
        self.assertFalse(result, "The sudoku board with a subgrid duplicate should fail verification.")


if __name__ == '__main__':
    unittest.main()
