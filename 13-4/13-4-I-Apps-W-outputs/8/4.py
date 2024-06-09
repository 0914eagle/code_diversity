
def get_sum_of_permutations(p, q):
    n = len(p)
    sum_of_permutations = [0] * n
    for i in range(n):
        sum_of_permutations[i] = (p[i] + q[i]) % n
    return sum_of_permutations

