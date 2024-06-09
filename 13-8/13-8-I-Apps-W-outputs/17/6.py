
def max_clique(A):
    # Initialize a dictionary to store the clique size for each number
    clique_sizes = {}
    # Iterate over the numbers in the set
    for num in A:
        # Initialize the clique size for the current number to 1
        clique_size = 1
        # Iterate over the numbers that are divisible by the current number
        for divisor in A:
            if num % divisor == 0 and divisor != num:
                # If the current number is divisible by a number that is not equal to it,
                # and the clique size for that number is greater than the current clique size,
                # update the clique size for the current number
                clique_size = max(clique_size, clique_sizes.get(divisor, 1) + 1)
        # Add the clique size for the current number to the dictionary
        clique_sizes[num] = clique_size
    # Return the maximum clique size among all the numbers
    return max(clique_sizes.values())

