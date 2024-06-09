
def solve(N, K, X, Q, L, R):
    seq = [0] * N
    for i in range(K):
        jump = X[i]
        for j in range(N):
            if j % jump == 0:
                seq[j] += 1
    result = []
    for i in range(Q):
        result.append(sum(seq[L[i]:R[i]+1]))
    return result

