
def solve(N, A, B):
    # Initialize a list to store the permutation
    perm = list(range(1, N+1))
    # Initialize a list to store the values of g(i) for each i
    g = [0] * (N+1)
    # Set the value of g(1) to A
    g[1] = A
    # Iterate through the rest of the permutation
    for i in range(2, N+1):
        # If the value of g(i-1) is A, set the value of g(i) to B
        if g[i-1] == A:
            g[i] = B
        # Otherwise, set the value of g(i) to A
        else:
            g[i] = A
    # Return the permutation
    return perm

