
def find_permutations(n):
    # Initialize two empty lists to store the permutations
    p = []
    q = []
    
    # Iterate from 1 to N
    for i in range(1, n+1):
        # Check if i is a power of 2
        if i & (i-1) == 0:
            # If i is a power of 2, add it to the end of p
            p.append(i)
        else:
            # If i is not a power of 2, add it to the end of q
            q.append(i)
    
    # Reverse the order of p
    p.reverse()
    
    # Return the permutations
    return p, q

