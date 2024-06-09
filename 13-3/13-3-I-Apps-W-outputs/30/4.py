
def solve(n, b):
    # Check if the sequence is strictly increasing
    for i in range(1, n):
        if b[i] <= b[i-1]:
            return "No"
    
    # Check if the sequence is a permutation of the original sequence
    b_set = set(b)
    if len(b_set) != n:
        return "No"
    
    # Find a valid permutation
    b_perm = list(b)
    for i in range(n):
        if b_perm[i] != b[i]:
            b_perm[i] = b[i]
            break
    
    return "Yes\n" + " ".join(map(str, b_perm))

