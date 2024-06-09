
def permutation_sum(p, q):
    n = len(p)
    sum_permutation = [0] * n
    for i in range(n):
        sum_permutation[i] = (p[i] + q[i]) % n
    return sum_permutation

