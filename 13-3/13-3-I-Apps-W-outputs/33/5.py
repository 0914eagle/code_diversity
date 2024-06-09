
def find_permutations(N):
    # Initialize the permutations as empty lists
    p = []
    q = []
    
    # Iterate from 1 to N
    for i in range(1, N+1):
        # Check if i is not equal to its index in p
        if i != len(p):
            # Add i to the end of p
            p.append(i)
        # Check if i is not equal to its index in q
        if i != len(q) and i & i == 0:
            # Add i to the end of q
            q.append(i)
    
    # Return the permutations
    return p, q

