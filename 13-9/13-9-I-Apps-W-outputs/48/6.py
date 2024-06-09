
def solve(N, S, T, U, V):
    # Initialize the matrix with all zeros
    a = [[0] * N for _ in range(N)]

    # Loop through each row and column
    for i in range(N):
        for j in range(N):
            # If S[i] = 0, set the element to U[i]
            if S[i] == 0:
                a[i][j] = U[i]
            # If S[i] = 1, set the element to V[j]
            if S[i] == 1:
                a[i][j] = V[j]
            # If T[j] = 0, set the element to U[j]
            if T[j] == 0:
                a[i][j] = U[j]
            # If T[j] = 1, set the element to V[j]
            if T[j] == 1:
                a[i][j] = V[j]

    # Return the matrix
    return a

