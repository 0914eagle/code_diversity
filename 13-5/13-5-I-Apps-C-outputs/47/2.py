
def solve(x, y):
    # Initialize the first two rows of the array
    f = [[0, 1], [1, 1]]

    # Fill in the rest of the array using the recurrence relation
    for i in range(2, x+1):
        for j in range(1, y+1):
            f[i][j] = (f[i-1][j] + f[i][j-1]) % 1000000007

    return f[x][y]

