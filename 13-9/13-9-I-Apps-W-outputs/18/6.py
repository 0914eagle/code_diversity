
def solve(A, B, k, m):
    if len(A) < k or len(B) < m:
        return "NO"
    for i in range(k):
        for j in range(m):
            if A[i] >= B[j]:
                return "NO"
    return "YES"

