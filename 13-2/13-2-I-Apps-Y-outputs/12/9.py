
def solve(permutation):
    n = len(permutation)
    # Swap adjacent elements to move the smallest element to the first position
    for i in range(n-1):
        if permutation[i] > permutation[i+1]:
            permutation[i], permutation[i+1] = permutation[i+1], permutation[i]
    # Swap elements in the first two positions to move the second smallest element to the second position
    if permutation[0] > permutation[1]:
        permutation[0], permutation[1] = permutation[1], permutation[0]
    return ''.join(str(i) for i in permutation)

