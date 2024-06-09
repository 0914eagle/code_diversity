
def solve(permutation):
    n = len(permutation)
    # Swap adjacent elements until the permutation is sorted
    for i in range(n-1):
        if permutation[i] > permutation[i+1]:
            permutation[i], permutation[i+1] = permutation[i+1], permutation[i]
    return permutation

