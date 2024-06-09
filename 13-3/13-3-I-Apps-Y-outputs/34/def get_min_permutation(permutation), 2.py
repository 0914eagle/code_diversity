
def get_min_permutation(permutation):
    n = len(permutation)
    for i in range(n-1):
        if permutation[i] > permutation[i+1]:
            permutation[i], permutation[i+1] = permutation[i+1], permutation[i]
    return permutation

