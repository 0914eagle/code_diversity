
def find_permutations(N):
    # Initialize the permutations as empty lists
    p = []
    q = []
    
    # Iterate from 1 to N
    for i in range(1, N+1):
        # Check if i is not equal to its index in the permutation
        if i != N:
            # Add i to the permutation p
            p.append(i)
            # Add i to the permutation q
            q.append(i)
        else:
            # Add N to the permutation p
            p.append(N)
            # Add N to the permutation q
            q.append(N)
    
    # Return the permutations
    return p, q

