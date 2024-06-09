
def solve(N, A, B):
    # Initialize a list to store the permutation
    perm = list(range(1, N+1))
    # Initialize a list to store the values of g(i) for each i
    g = [0] * (N+1)
    # Initialize a list to store the values of f(i, j) for each i and j
    f = [[0] * (N+1) for _ in range(N+1)]
    
    # Compute the values of f(i, j) for each i and j
    for i in range(1, N+1):
        for j in range(1, N+1):
            if j == 1:
                f[i][j] = perm[i-1]
            else:
                f[i][j] = f[perm[i-1]][j-1]
    
    # Compute the values of g(i) for each i
    for i in range(1, N+1):
        g[i] = 1
        for j in range(1, N+1):
            if f[i][j] == i:
                g[i] = j
                break
    
    # Check if a permutation exists with the given constraints
    for i in range(1, N+1):
        if g[i] not in [A, B]:
            return -1
    
    # If a permutation exists, return it
    return perm

