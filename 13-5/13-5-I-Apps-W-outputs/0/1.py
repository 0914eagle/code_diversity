
def get_maximum_sum(n):
    permutation = list(range(1, n+1))
    remainder = [i%j for i, j in enumerate(permutation, 1)]
    return sum(remainder)

