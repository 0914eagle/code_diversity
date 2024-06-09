
def solve(N, S, T, U, V):
    # Initialize the matrix with all zeros
    a = [[0] * N for _ in range(N)]

    # Populate the matrix based on the given conditions
    for i in range(N):
        for j in range(N):
            if S[i] == 0:
                a[i][j] = U[i] & V[j]
            else:
                a[i][j] = U[i] | V[j]

    # Check if the matrix satisfies the conditions
    for i in range(N):
        for j in range(N):
            if T[j] == 0 and a[i][j] != U[i]:
                return -1
            if T[j] == 1 and a[i][j] != V[j]:
                return -1

    return a

