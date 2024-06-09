
def solve(A, B, k, m):
    if k > len(A) or m > len(B):
        return "NO"
    
    for i in range(k):
        for j in range(m):
            if A[i] >= B[j]:
                return "NO"
    
    return "YES"

