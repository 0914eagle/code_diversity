
def solve(N, K, M, A):
    total = sum(A)
    average = total / (N-1)
    if average >= M:
        return -1
    else:
        return M - average

