
def get_max_beauty(n):
    # Initialize a list to store the permutations
    permutations = []
    
    # Iterate from 0 to n
    for i in range(n + 1):
        # Get the permutation of integers from 0 to n
        permutation = list(range(n + 1))
        permutation[i] = permutation[0]
        permutation.pop(0)
        
        # Calculate the beauty of the permutation
        beauty = 0
        for j in range(n):
            beauty += (j ^ permutation[j])
        
        # Add the permutation to the list of permutations
        permutations.append((beauty, permutation))
    
    # Return the permutation with the maximum beauty
    return max(permutations)[1]

