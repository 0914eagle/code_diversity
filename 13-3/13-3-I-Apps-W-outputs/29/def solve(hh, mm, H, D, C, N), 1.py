
def solve(hh, mm, H, D, C, N):
    # Calculate the time until the next store opening
    if hh < 20:
        time_until_store_opening = 20 - hh
    else:
        time_until_store_opening = 24 - hh + 20
    
    # Calculate the number of minutes until the cat is fed
    minutes_until_fed = (H - 1) // D + 1
    
    # Calculate the number of buns needed to feed the cat
    buns_needed = (minutes_until_fed * D) // N
    
    # Calculate the total cost of the buns
    total_cost = buns_needed * C
    
    # Apply the discount if the store is open
    if time_until_store_opening == 0:
        total_cost *= 0.8
    
    # Return the total cost rounded to three decimal places
    return round(total_cost, 3)

