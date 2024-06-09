
def solve(n, s, t, u, v):
    # Initialize the matrix with all zeros
    a = [[0] * n for _ in range(n)]

    # Populate the matrix based on the conditions given
    for i in range(n):
        for j in range(n):
            if s[i] == 0:
                a[i][j] = u[i] & v[j]
            elif s[i] == 1:
                a[i][j] = u[i] | v[j]
            if t[j] == 0:
                a[i][j] &= v[j]
            elif t[j] == 1:
                a[i][j] |= v[j]

    # Check if the matrix satisfies the conditions
    for i in range(n):
        for j in range(n):
            if a[i][j] < 0 or a[i][j] >= 2 ** 64:
                return -1

    return a

