
def solve(N, K, M, A):
    total = sum(A)
    avg = total / (N-1)
    if M <= avg:
        return -1
    else:
        return M - avg

