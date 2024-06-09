
def find_largest_perfect_power(x):
    # Initialize a list to store the perfect powers
    perfect_powers = []
    
    # Loop through all integers from 1 to the square root of x
    for i in range(1, int(x**0.5) + 1):
        # Check if i is a perfect power
        if x % i == 0:
            # Add i to the list of perfect powers
            perfect_powers.append(i)
    
    # Return the largest perfect power
    return max(perfect_powers)

