
def get_largest_perfect_power(x):
    # Initialize a list to store the perfect powers
    perfect_powers = []
    
    # Loop through all integers from 1 to x
    for i in range(1, x + 1):
        # Check if the integer is a perfect power
        if is_perfect_power(i):
            # If it is a perfect power, add it to the list
            perfect_powers.append(i)
    
    # Return the largest perfect power in the list
    return max(perfect_powers)

def is_perfect_power(n):
    # Initialize a flag to indicate if n is a perfect power
    is_pp = False
    
    # Loop through all integers from 1 to the square root of n
    for i in range(1, int(n ** 0.5) + 1):
        # Check if i is a factor of n
        if n % i == 0:
            # If it is, check if the other factor is also an integer
            if n // i == i:
                # If it is, n is a perfect power
                is_pp = True
                break
    
    # Return the flag
    return is_pp

