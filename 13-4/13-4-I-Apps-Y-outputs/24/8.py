
def solve(A, B):
    N = len(A)
    M = len(B)
    result = ['.' * N for _ in range(M)]
    for i in range(N):
        if A[i] in B:
            j = B.index(A[i])
            result[j] = A[i] + result[j][1:]
    return '\n'.join(result)

