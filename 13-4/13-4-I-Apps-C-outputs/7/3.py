
def solve(N, A, B):
    # Initialize a list to store the permutation
    perm = list(range(1, N+1))
    # Initialize a list to store the values of g(i) for each i
    g = [0] * (N+1)
    # Initialize a set to keep track of the values of g(i) that have been used
    used = set()
    
    # Loop through each element of the permutation
    for i in range(N):
        # If the value of g(i) has not been used, use it
        if g[i] not in used:
            g[i] = A
            used.add(A)
        # Otherwise, use the other value
        else:
            g[i] = B
            used.add(B)
    
    # Check if the permutation satisfies the condition
    for i in range(N):
        if g[i] != A and g[i] != B:
            return -1
    
    return perm

