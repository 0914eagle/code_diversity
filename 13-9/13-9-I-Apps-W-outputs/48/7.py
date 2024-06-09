
def solve(N, S, T, U, V):
    # Initialize the matrix with all zeros
    a = [[0] * N for _ in range(N)]

    # Populate the matrix based on the conditions
    for i in range(N):
        for j in range(N):
            if S[i] == 0:
                a[i][j] = U[i] & V[j]
            elif S[i] == 1:
                a[i][j] = U[i] | V[j]
            if T[j] == 0:
                a[i][j] = a[i][j] & U[i]
            elif T[j] == 1:
                a[i][j] = a[i][j] | U[i]

    # Check if the matrix satisfies the conditions
    for i in range(N):
        for j in range(N):
            if S[i] == 0 and a[i][j] != U[i]:
                return -1
            elif S[i] == 1 and a[i][j] != U[i]:
                return -1
            if T[j] == 0 and a[i][j] != V[j]:
                return -1
            elif T[j] == 1 and a[i][j] != V[j]:
                return -1

    return a

