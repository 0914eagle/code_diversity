
def get_x_and_y(divisors):
    # Initialize x and y to 1
    x = 1
    y = 1
    
    # Iterate through the divisors
    for d in divisors:
        # If d is not a divisor of both x and y, find the next divisor of x or y
        if d not in [x, y]:
            if d % x == 0:
                y *= d
            else:
                x *= d
    
    # Return the final values of x and y
    return x, y

