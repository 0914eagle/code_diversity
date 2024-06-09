
def solve(A, B, k, m):
    if k == 0 and m == 0:
        return "YES"
    if k == 0 or m == 0:
        return "NO"
    if A[0] < B[0]:
        return solve(A[1:], B, k-1, m)
    if B[0] < A[0]:
        return solve(A, B[1:], k, m-1)
    return "NO"

