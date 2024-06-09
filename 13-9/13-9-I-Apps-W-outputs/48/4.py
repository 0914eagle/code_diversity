
def solve(N, S, T, U, V):
    # Initialize the matrix with all zeros
    a = [[0] * N for _ in range(N)]

    # Loop through each row and column
    for i in range(N):
        for j in range(N):
            # If S[i] is 0, set the element to U[i]
            if S[i] == 0:
                a[i][j] = U[i]
            # If T[j] is 0, set the element to V[j]
            if T[j] == 0:
                a[i][j] = V[j]

    # Check if the matrix satisfies the conditions
    for i in range(N):
        # Calculate the bitwise AND of the elements in the i-th row
        row_and = a[i][0]
        for j in range(1, N):
            row_and &= a[i][j]
        # If the bitwise AND is not equal to U[i], return -1
        if row_and != U[i]:
            return -1
        # Calculate the bitwise OR of the elements in the i-th row
        row_or = a[i][0]
        for j in range(1, N):
            row_or |= a[i][j]
        # If the bitwise OR is not equal to V[i], return -1
        if row_or != V[i]:
            return -1
        # Calculate the bitwise AND of the elements in the i-th column
        col_and = a[0][i]
        for j in range(1, N):
            col_and &= a[j][i]
        # If the bitwise AND is not equal to U[i], return -1
        if col_and != U[i]:
            return -1
        # Calculate the bitwise OR of the elements in the i-th column
        col_or = a[0][i]
        for j in range(1, N):
            col_or |= a[j][i]
        # If the bitwise OR is not equal to V[i], return -1
        if col_or != V[i]:
            return -1

    # If we reach this point, the matrix satisfies the conditions, so return it
    return a

