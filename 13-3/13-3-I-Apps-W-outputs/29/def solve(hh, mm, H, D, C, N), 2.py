
def solve(hh, mm, H, D, C, N):
    # Calculate the total hunger level after the given time
    total_hunger = H + (mm * D) + (hh * 60 * D)
    
    # Calculate the number of buns needed to feed the cat
    num_buns = total_hunger // N
    
    # Calculate the cost of the buns
    cost = num_buns * C
    
    # Apply the discount if the time is between 20:00 and 23:59
    if hh >= 20:
        cost = cost - (cost * 0.2)
    
    return cost

