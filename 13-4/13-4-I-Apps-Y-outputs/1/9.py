
def largest_perfect_power(x):
    # Initialize a list to store the perfect powers
    perfect_powers = []
    
    # Loop through all integers from 1 to x
    for i in range(1, x + 1):
        # Find the square root of i
        root = int(i ** 0.5)
        
        # Check if the square root is an integer
        if root ** 2 == i:
            # If it is an integer, add it to the list of perfect powers
            perfect_powers.append(i)
    
    # Return the largest perfect power in the list
    return max(perfect_powers)

