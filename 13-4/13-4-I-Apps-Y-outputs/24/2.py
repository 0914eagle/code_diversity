
def solve(A, B):
    N = len(A)
    M = len(B)
    grid = [["."]*N for _ in range(M)]
    for i in range(N):
        if A[i] in B:
            j = B.index(A[i])
            grid[j][i] = A[i]
            break
    for j in range(M):
        if B[j] in A:
            i = A.index(B[j])
            grid[j][i] = B[j]
    return "\n".join(["".join(row) for row in grid])

