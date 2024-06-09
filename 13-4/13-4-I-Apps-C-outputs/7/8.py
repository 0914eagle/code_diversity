
def solve(N, A, B):
    # Initialize a list to store the permutation
    perm = list(range(1, N+1))
    # Initialize a list to store the values of g(i) for each i
    g = [0] * (N+1)
    # Initialize a set to keep track of the values of g(i) that have been used
    used = set()
    
    # Iterate through the permutation and calculate the values of g(i)
    for i in range(1, N+1):
        # If the value of g(i) has already been used, return -1
        if g[i] in used:
            return -1
        # Otherwise, calculate the value of g(i) and add it to the set of used values
        g[i] = perm[i] if i == 1 else g[perm[i]]
        used.add(g[i])
    
    # If the set of used values does not contain both A and B, return -1
    if A not in used or B not in used:
        return -1
    
    # Otherwise, return the permutation
    return perm

