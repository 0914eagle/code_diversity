
def find_permutations(n):
    # Initialize the permutations as empty lists
    p = []
    q = []
    
    # Iterate from 1 to N
    for i in range(1, n+1):
        # Check if i is not equal to its index in the permutation
        if i != n:
            # Add i to the permutation
            p.append(i)
        # Check if i is not equal to its index in the permutation and its bitwise AND with i is not zero
        if i != n and i & i != 0:
            # Add i to the permutation
            q.append(i)
    
    # Return the permutations
    return p, q

