
def solve(n, divisors):
    # Initialize x and y to 1
    x, y = 1, 1
    
    # Iterate through the list of divisors
    for d in divisors:
        # If d is not a divisor of both x and y, find the next divisor of x or y that is also a divisor of the other number
        if d not in [x, y]:
            for i in range(1, n+1):
                if i in [x, y] or i % x != 0 or i % y != 0:
                    continue
                d = i
                break
        # Update x and y based on the divisor found
        if d not in [x, y]:
            x *= d
        else:
            y *= d
    
    return x, y

