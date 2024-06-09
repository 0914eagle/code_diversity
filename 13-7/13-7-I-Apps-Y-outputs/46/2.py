
def largest_perfect_power(x):
    # Find the smallest perfect power that is greater than or equal to x
    power = 1
    while power <= x:
        power *= 2
    
    # Check if the previous power is a perfect power
    if power / 2 >= x:
        return power / 2
    
    # If not, then the previous power is not a perfect power
    # So, we need to find the next smaller power that is a perfect power
    power //= 2
    while power >= 1:
        if x % power == 0:
            return power
        power //= 2
    
    # If we reach here, then no perfect power was found
    return 1

