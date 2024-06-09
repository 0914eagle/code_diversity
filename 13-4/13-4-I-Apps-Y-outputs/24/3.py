
def solve(A, B):
    N = len(A)
    M = len(B)
    result = ["."] * N
    for i in range(N):
        if A[i] in B:
            result[i] = A[i]
            break
    for i in range(M):
        if B[i] in A:
            result[i] = B[i]
            break
    return "\n".join(result)

