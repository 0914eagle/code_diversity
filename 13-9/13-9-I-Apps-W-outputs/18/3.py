
def solve(A, B, k, m):
    if k == 0 and m == 0:
        return "YES"
    if k == 0 or m == 0:
        return "NO"
    if A[k-1] < B[m-1]:
        return solve(A, B, k-1, m)
    if B[m-1] < A[k-1]:
        return solve(A, B, k, m-1)
    return "NO"

