
def get_largest_xor_sum(n, k):
    # Convert the input numbers to lists
    n = list(map(int, str(n)))
    k = list(map(int, str(k)))
    
    # Initialize the xor sum to 0
    xor_sum = 0
    
    # Iterate through the list of candies
    for i in range(len(n)):
        # Check if the current candy is within the limit
        if i < k:
            # Add the current candy to the xor sum
            xor_sum ^= n[i]
    
    # Return the largest xor sum
    return xor_sum

