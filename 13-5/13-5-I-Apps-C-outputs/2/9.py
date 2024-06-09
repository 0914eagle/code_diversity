
def solve(N, A, B):
    total_ham = 0
    for i in range(N):
        if B[i] != 0:
            total_ham += A[i] / B[i]
    return total_ham

