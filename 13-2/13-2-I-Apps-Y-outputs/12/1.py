
def get_lexicographically_min_permutation(permutation):
    n = len(permutation)
    # Perform Bubble Sort to sort the permutation in non-decreasing order
    for i in range(n-1):
        for j in range(0, n-i-1):
            if permutation[j] > permutation[j+1]:
                permutation[j], permutation[j+1] = permutation[j+1], permutation[j]
    return permutation

