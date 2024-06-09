
def get_special_sums(N, K, X, Q, L, R):
    seq = [0] * N
    for i in range(K):
        jump = X[i]
        for j in range(N):
            if j % jump == 0:
                seq[j] += 1
    
    special_sums = []
    for i in range(Q):
        left = L[i]
        right = R[i]
        special_sums.append(sum(seq[left:right+1]))
    
    return special_sums

