
def solve(H, n, d):
    # Calculate the total change in hp for each round
    total_change = sum(d)
    
    # If the total change is positive, the monster will die
    if total_change > 0:
        return -1
    
    # If the total change is negative, the monster will survive
    if total_change < 0:
        return n
    
    # If the total change is zero, the monster will survive if its hp is greater than zero
    if H > 0:
        return -1
    
    # If the total change is zero and the monster's hp is zero, the battle will last infinitely
    return n

