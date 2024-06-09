
def solve(N, D, X, *A):
    total_pieces = 0
    for i in range(N):
        total_pieces += (D - A[i]) // (A[i] + 1)
    return X + total_pieces

