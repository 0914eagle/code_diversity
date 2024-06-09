
def get_maximum_clique(A):
    # Initialize a dictionary to store the clique size for each number
    clique_sizes = {}
    # Iterate over the numbers in A
    for num in A:
        # Initialize the clique size for the current number to 1
        clique_size = 1
        # Iterate over the numbers in A that are divisible by the current number
        for div in [x for x in A if num % x == 0]:
            # If the current number is divisible by another number in A, add the clique size of that number to the current number's clique size
            clique_size += clique_sizes.get(div, 1)
        # Add the current number's clique size to the dictionary
        clique_sizes[num] = clique_size
    # Return the maximum clique size in the dictionary
    return max(clique_sizes.values())

