
def solve(N, S, T, U, V):
    # Initialize the matrix with all zeros
    a = [[0] * N for _ in range(N)]

    # Fill in the matrix based on the conditions
    for i in range(N):
        for j in range(N):
            if S[i] == 0:
                a[i][j] = U[i] & V[j]
            elif S[i] == 1:
                a[i][j] = U[i] | V[j]
            if T[j] == 0:
                a[i][j] = a[i][j] & U[i]
            elif T[j] == 1:
                a[i][j] = a[i][j] | V[j]

    # Check if the matrix satisfies the conditions
    for i in range(N):
        for j in range(N):
            if a[i][j] < 0 or a[i][j] >= 2 ** 64:
                return -1

    return a

