
def get_largest_perfect_power(x):
    # Initialize a list to store the perfect powers
    perfect_powers = []
    
    # Loop through all integers from 1 to x
    for i in range(1, x + 1):
        # Check if the integer is a perfect power
        if is_perfect_power(i):
            # If it is, add it to the list of perfect powers
            perfect_powers.append(i)
    
    # Return the largest perfect power in the list
    return max(perfect_powers)

def is_perfect_power(n):
    # Initialize a variable to store the result
    result = False
    
    # Loop through all integers from 1 to the square root of n
    for i in range(1, int(n ** 0.5) + 1):
        # Check if i is a factor of n
        if n % i == 0:
            # If it is, return True
            result = True
            break
    
    # Return the result
    return result

# Test the function with the given input
x = int(input())
print(get_largest_perfect_power(x))

