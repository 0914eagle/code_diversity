
def solve(n, m):
    # convert the integer to a string
    n = str(n)
    
    # initialize the minimum remainder to a large value
    min_remainder = 10**8
    
    # loop through all cyclic shifts of the integer
    for i in range(len(n)):
        # calculate the remainder of the current shift when divided by m
        remainder = int(n[i:]) % m
        
        # update the minimum remainder if necessary
        min_remainder = min(min_remainder, remainder)
    
    return min_remainder

