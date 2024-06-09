
def solve(A, B):
    N = len(A)
    M = len(B)
    grid = ['.' * N for _ in range(M)]
    for i in range(N):
        if A[i] in B:
            grid[B.index(A[i])] = A[i]
    return '\n'.join(grid)

