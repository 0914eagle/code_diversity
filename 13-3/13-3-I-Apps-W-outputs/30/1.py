
def solve(n, b):
    # Check if the sequence is strictly increasing
    for i in range(1, n):
        if b[i] <= b[i-1]:
            return "No"
    
    # Check if the sequence is a permutation of the original sequence
    b_set = set(b)
    if len(b_set) != n:
        return "No"
    
    # Find a permutation of the sequence that is strictly increasing
    b_perm = list(b)
    for i in range(n-1):
        for j in range(i+1, n):
            if b_perm[i] > b_perm[j]:
                b_perm[i], b_perm[j] = b_perm[j], b_perm[i]
                break
    
    return "Yes\n" + " ".join(str(x) for x in b_perm)

