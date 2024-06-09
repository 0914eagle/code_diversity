
def get_max_sum(A):
    n = len(A)
    if n == 1:
        return A[0]
    if n == 2:
        return max(A[0], A[1])
    if n % 2 == 0:
        return max(A[0] + A[2], A[1] + A[3])
    else:
        return max(A[0] + A[2] + A[4], A[1] + A[3] + A[5])

