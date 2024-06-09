
def get_max_clique_size(A):
    # Initialize a dictionary to store the clique size for each number
    clique_sizes = {}
    # Initialize the maximum clique size
    max_clique_size = 0
    
    # Iterate over the numbers in A
    for a in A:
        # Initialize the clique size for the current number
        clique_size = 1
        # Iterate over the numbers in A that are divisible by the current number
        for b in A:
            if a % b == 0:
                # Increment the clique size for the current number
                clique_size += 1
        # Update the maximum clique size
        max_clique_size = max(max_clique_size, clique_size)
    
    # Return the maximum clique size
    return max_clique_size

