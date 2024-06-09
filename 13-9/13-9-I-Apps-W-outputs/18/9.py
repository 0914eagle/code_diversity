
def solve(A, B, k, m):
    if len(A) < k or len(B) < m:
        return "NO"
    
    i = 0
    j = 0
    count = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
            count += 1
        elif A[i] > B[j]:
            j += 1
        else:
            i += 1
            j += 1
    
    if count == k:
        return "YES"
    else:
        return "NO"

