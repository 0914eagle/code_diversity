
import math

def solve(n, m, mod, matrix):
    # Initialize variables
    rows, cols = [], []
    count = 0

    # Convert the input matrix into a list of lists
    for i in range(m):
        rows.append(list(matrix[i]))

    # Check if the input matrix is valid
    for row in rows:
        if len(row) != n:
            return -1
        for col in range(n):
            if row[col] not in ["0", "1"]:
                return -1

    # Count the number of ones in each row and column
    for i in range(n):
        rows.append([row[i] for row in rows])
        cols.append([row[i] for row in zip(*rows)])

    # Check if the number of ones in each row and column is equal to 2
    for row in rows:
        if row.count("1") != 2:
            return 0
    for col in cols:
        if col.count("1") != 2:
            return 0

    # Calculate the number of special nxn matrices
    for i in range(2**n):
        row = bin(i)[2:].zfill(n)
        if rows[0] == row:
            count += 1

    # Return the remainder after dividing the count by the modulus
    return count % mod

