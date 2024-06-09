
def solve(n, b):
    # Check if the sequence is already strictly increasing
    if all(b[i] < b[i+1] for i in range(n-1)):
        return "Yes\n" + " ".join(str(x) for x in b)
    
    # Find all possible permutations of the sequence
    permutations = []
    for perm in itertools.permutations(b):
        # Check if the permutation is strictly increasing
        if all(perm[i] < perm[i+1] for i in range(n-1)):
            permutations.append(perm)
    
    # If there are no valid permutations, return "No"
    if not permutations:
        return "No"
    
    # Otherwise, return any valid permutation
    return "Yes\n" + " ".join(str(x) for x in permutations[0])

