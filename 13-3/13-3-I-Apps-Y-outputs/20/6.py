
def solve(n, divisors):
    # Initialize x and y to 1
    x, y = 1, 1
    
    # Iterate through the divisors
    for d in divisors:
        # If d is not a divisor of both x and y, find the next divisor of x or y
        if d not in [x, y]:
            if d % x == 0:
                y *= d
            else:
                x *= d
        # If d is a divisor of both x and y, find the next divisor of x or y
        else:
            if d % x == 0:
                y *= d
            else:
                x *= d
    
    return x, y

