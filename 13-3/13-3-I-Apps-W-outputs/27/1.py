
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

    # Check if the number of ones in each row and column is equal to 2
    if all(row == 2 for row in rows) and all(col == 2 for col in cols):
        num_matrices += 1

    # Return the remainder after dividing the number of matrices by the given modulus
    return num_matrices % mod

