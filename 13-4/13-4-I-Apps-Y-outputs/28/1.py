
def solve(N, A, B, C):
    altars = set()
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if A[i] < A[j] and A[j] < A[k] and B[i] < B[j] and B[j] < B[k] and C[i] < C[j] and C[j] < C[k]:
                    altars.add((i, j, k))
    return len(altars)

