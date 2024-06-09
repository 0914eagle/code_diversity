
def permutation_sum(p, q):
    n = len(p)
    sum_perm = [0] * n
    for i in range(n):
        sum_perm[i] = (p[i] + q[i]) % n
    return sum_perm

