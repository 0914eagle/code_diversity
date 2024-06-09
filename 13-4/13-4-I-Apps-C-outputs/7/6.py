
def solve(N, A, B):
    # Initialize a list to store the permutation
    perm = list(range(1, N+1))
    # Initialize a list to store the values of g(i) for each i
    g = [0] * (N+1)
    # Initialize a set to keep track of the values of g(i) that have been used
    used = set()
    # Loop through each i from 1 to N
    for i in range(1, N+1):
        # If g(i) has not been used before, use it
        if i not in used:
            # Add the value of g(i) to the set of used values
            used.add(g[i])
            # If the value of g(i) is A or B, use it for the permutation
            if g[i] in [A, B]:
                perm[i] = g[i]
            # Otherwise, use the next unused value of g(i)
            else:
                perm[i] = min(used)
        # Update the value of g(i) for the next iteration
        g[i] = perm[i]
    # If not all values of g(i) have been used, the permutation is not possible
    if len(used) != N:
        return -1
    # Otherwise, return the permutation
    return perm

