
def solve(n):
    # Initialize a 2D array to store the table
    table = [[0] * n for _ in range(n)]

    # Fill in the first row and column with ones
    for i in range(n):
        table[i][0] = 1
        table[0][i] = 1

    # Fill in the remaining elements using the given formula
    for i in range(1, n):
        for j in range(1, n):
            table[i][j] = table[i - 1][j] + table[i][j - 1]

    # Return the maximum value in the table
    return max(max(row) for row in table)

