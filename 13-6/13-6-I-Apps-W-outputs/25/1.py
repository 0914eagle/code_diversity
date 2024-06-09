
def solve(N, X, M):
    A = [X]
    for i in range(N-1):
        A.append(pow(A[i], 2, M))
    return sum(A)

