
import math

def solve(n, m, mod, matrix):
    # Initialize variables
    rows, cols = [], []
    total_ones = 0
    num_matrices = 0

    # Convert the input matrix into a list of lists
    matrix = [list(row) for row in matrix]

    # Count the number of ones in each row and column
    for i in range(n):
        rows.append(matrix[i].count("1"))
        cols.append(matrix[i].count("1"))
        total_ones += matrix[i].count("1")

    # Check if the matrix is special
    if total_ones != n:
        return 0

    # Count the number of special matrices
    for i in range(m):
        for j in range(i+1, m):
            if rows[i] == rows[j] and cols[i] == cols[j]:
                num_matrices += 1

    # Calculate the remainder
    remainder = num_matrices % mod

    return remainder

