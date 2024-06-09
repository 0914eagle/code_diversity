
def largest_perfect_power(x):
    # Initialize a list to store the perfect powers
    perfect_powers = []
    
    # Iterate from 1 to the square root of x
    for i in range(1, int(x**0.5) + 1):
        # Check if i is a perfect power
        if x % i == 0:
            # Add the perfect power to the list
            perfect_powers.append(i)
    
    # Return the largest perfect power
    return max(perfect_powers)

