
def something(seq, jump):
    for i in range(len(seq)):
        if i % jump == 0:
            seq[i] += 1
    return seq

def solve(N, K, X, Q, L, R):
    seq = [0] * N
    for i in range(K):
        seq = something(seq, X[i])
    result = []
    for i in range(Q):
        result.append(sum(seq[L[i]:R[i]+1]))
    return result

