
def solve(N, K, X, Q, L, R):
    seq = [0] * N
    for i in range(K):
        for j in range(X[i]):
            seq[j] += 1
    result = []
    for i in range(Q):
        result.append(sum(seq[L[i]:R[i]+1]))
    return result

