
def get_x_and_y(divisors):
    # Initialize x and y to 1
    x = 1
    y = 1
    
    # Iterate through the list of divisors
    for divisor in divisors:
        # If the divisor is not a multiple of x, multiply x by the divisor
        if divisor % x != 0:
            x *= divisor
        # If the divisor is not a multiple of y, multiply y by the divisor
        if divisor % y != 0:
            y *= divisor
    
    # Return x and y
    return x, y

