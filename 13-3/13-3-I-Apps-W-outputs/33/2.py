
def find_permutations(n):
    # Initialize the permutations as empty lists
    p = []
    q = []
    
    # Iterate from 1 to N
    for i in range(1, n+1):
        # Check if i is not equal to its index in p
        if i != p.index(i) + 1:
            # Add i to p
            p.append(i)
        # Check if i is not equal to its index in q
        if i != q.index(i) + 1 and q.index(i) + 1 != 0:
            # Add i to q
            q.append(i)
    
    # Return the permutations
    return p, q

