
import itertools

def num_permutations_modulo(n, k, p):
    return len(list(itertools.permutations(range(n)))) % p

