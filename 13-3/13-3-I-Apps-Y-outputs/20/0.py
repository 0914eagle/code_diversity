
def solve(n, divisors):
    # Initialize x and y to 1
    x = 1
    y = 1
    
    # Iterate through the list of divisors
    for divisor in divisors:
        # If the divisor is not already a factor of x or y, add it to the appropriate number
        if divisor not in str(x):
            x *= divisor
        if divisor not in str(y):
            y *= divisor
    
    # Return the final values of x and y
    return x, y

