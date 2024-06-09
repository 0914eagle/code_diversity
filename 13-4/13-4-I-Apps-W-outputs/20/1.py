
def find_permutations(n):
    # Initialize a list to store the permutations
    permutations = []
    
    # Iterate from 1 to N
    for i in range(1, n + 1):
        # Initialize a list to store the current permutation
        current_permutation = []
        
        # Iterate from 1 to N
        for j in range(1, n + 1):
            # If i is not equal to j and i & j is not equal to 0, add j to the current permutation
            if i != j and i & j != 0:
                current_permutation.append(j)
        
        # If the current permutation has N elements, add it to the list of permutations
        if len(current_permutation) == n:
            permutations.append(current_permutation)
    
    # If no permutations were found, return "NO"
    if not permutations:
        return "NO"
    
    # Otherwise, return "YES" and the first permutation
    return "YES\n" + " ".join(map(str, permutations[0]))

