
def find_permutations(n):
    # Initialize the permutations as empty lists
    p = []
    q = []
    
    # Iterate from 1 to N
    for i in range(1, n+1):
        # If i is not equal to its index, it is a valid element for p
        if i != n:
            p.append(i)
        # If i is not equal to its index and i is not equal to 0, it is a valid element for q
        if i != n and i != 0:
            q.append(i)
    
    # Return the permutations
    return p, q

