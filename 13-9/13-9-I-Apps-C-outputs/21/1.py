
import itertools

def count_permutations(n, k):
    return len(list(itertools.permutations(range(1, n+1), k))) % (2**31 - 1)

