
def find_permutations(N):
    # Initialize the permutations as empty lists
    p = []
    q = []
    
    # Iterate from 1 to N
    for i in range(1, N+1):
        # If i is not equal to its index, add it to the permutation p
        if i != N:
            p.append(i)
        # If i is not equal to its index and its binary representation has at least one 1-bit, add it to the permutation q
        if i != N and bin(i).count("1") > 0:
            q.append(i)
    
    # If either permutation is empty, return "NO"
    if not p or not q:
        return "NO"
    
    # Otherwise, return "YES" and the permutations
    return "YES\n" + " ".join(map(str, p)) + "\n" + " ".join(map(str, q))
