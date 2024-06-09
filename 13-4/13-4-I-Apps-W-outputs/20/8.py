
def find_permutations(n):
    # Initialize two empty lists to store the permutations
    p = []
    q = []
    
    # Iterate from 1 to N
    for i in range(1, n+1):
        # Check if i is not equal to its index in the permutation
        if i != p.index(i) + 1:
            # If i is not equal to its index, add it to the permutation
            p.append(i)
        # Check if the bitwise AND of i and its index is not equal to 0
        if i & p.index(i) != 0:
            # If the bitwise AND is not equal to 0, add it to the permutation
            q.append(i)
    
    # If the length of the permutations is not equal to N, return "NO"
    if len(p) != n or len(q) != n:
        return "NO"
    
    # Otherwise, return "YES" and the permutations
    return "YES\n" + " ".join(map(str, p)) + "\n" + " ".join(map(str, q))

