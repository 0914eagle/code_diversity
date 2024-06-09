
import itertools

def get_permutation_count(n, k):
    return len(list(itertools.permutations(range(1, n+1), k))) % (2**31 - 1)

