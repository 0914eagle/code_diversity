
def solve(N, A, B):
    # Initialize a list to store the permutation
    perm = list(range(1, N+1))
    
    # Loop through each element in the permutation
    for i in range(N):
        # If the current element is equal to A or B, skip it
        if perm[i] in [A, B]:
            continue
        # Otherwise, find the next element in the permutation that is not equal to A or B
        # and swap it with the current element
        for j in range(i+1, N):
            if perm[j] in [A, B]:
                continue
            perm[i], perm[j] = perm[j], perm[i]
            break
    
    # If the permutation is valid, return it, otherwise return -1
    if set(perm) == set(range(1, N+1)):
        return perm
    else:
        return -1

