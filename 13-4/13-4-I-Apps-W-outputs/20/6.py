
def find_permutations(n):
    permutations = []
    for i in range(1, n+1):
        permutation = [i]
        for j in range(1, n+1):
            if j != i and j & i == 0:
                permutation.append(j)
        permutations.append(permutation)
    return permutations

