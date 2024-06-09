
def solve(n, s, t, u, v):
    # Initialize the matrix with all 0s
    a = [[0] * n for _ in range(n)]

    # Loop through each row and column
    for i in range(n):
        for j in range(n):
            # If S[i] is 0, set the element to U[i]
            if s[i] == 0:
                a[i][j] = u[i]
            # If S[i] is 1, set the element to V[j]
            elif s[i] == 1:
                a[i][j] = v[j]
            # If T[j] is 0, set the element to U[j]
            if t[j] == 0:
                a[i][j] = u[j]
            # If T[j] is 1, set the element to V[j]
            elif t[j] == 1:
                a[i][j] = v[j]

    # Return the matrix
    return a

