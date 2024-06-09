
def get_sorted_array_probability(n, k, a):
    # Calculate the number of possible permutations of the array
    num_permutations = 1
    for i in range(n):
        num_permutations *= n - i
    
    # Initialize the probability to 0
    probability = 0
    
    # Iterate over all possible permutations of the array
    for permutation in range(num_permutations):
        # Convert the permutation index to a binary string
        binary_string = bin(permutation)[2:]
        binary_string = binary_string.zfill(n)
        
        # Initialize a flag to indicate if the array is sorted
        is_sorted = True
        
        # Iterate over the elements of the array
        for i in range(n - 1):
            # If the elements are not in non-decreasing order, set the flag to False
            if binary_string[i] > binary_string[i + 1]:
                is_sorted = False
                break
        
        # If the array is sorted, add the probability of this permutation to the total probability
        if is_sorted:
            probability += 1
    
    # Return the probability divided by the number of possible permutations
    return probability / num_permutations

