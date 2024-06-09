
def get_x_and_y(divisors):
    # Initialize x and y as 1
    x = 1
    y = 1
    
    # Iterate through the list of divisors
    for divisor in divisors:
        # If the divisor is not a multiple of x and y, set x and y to be their least common multiple
        if divisor % x == 0 and divisor % y == 0:
            continue
        else:
            x = x * divisor // gcd(x, divisor)
            y = y * divisor // gcd(y, divisor)
    
    return x, y

