
def get_max_deliciousness(X, Y, A, B, C, p, q, r):
    # Initialize a two-dimensional table to store the results of subproblems
    table = [[0] * (Y + 1) for _ in range(X + 1)]

    # Fill the table with the values of the colorless apples
    for i in range(1, X + 1):
        for j in range(1, Y + 1):
            table[i][j] = max(table[i - 1][j], table[i][j - 1] + r[j - 1])

    # Fill the table with the values of the red apples
    for i in range(1, X + 1):
        for j in range(1, Y + 1):
            table[i][j] = max(table[i][j], table[i - 1][j - 1] + p[i - 1])

    # Fill the table with the values of the green apples
    for i in range(1, X + 1):
        for j in range(1, Y + 1):
            table[i][j] = max(table[i][j], table[i - 1][j - 1] + q[j - 1])

    # Return the maximum value in the last row of the table
    return table[X][Y]

