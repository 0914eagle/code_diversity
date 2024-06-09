
def solve(words):
    A, B = words.split()
    m, n = len(B), len(A)
    grid = [['.'] * n for _ in range(m)]
    for i in range(n):
        if A[i] in B:
            grid[B.index(A[i])][i] = A[i]
    return '\n'.join(''.join(row) for row in grid)

