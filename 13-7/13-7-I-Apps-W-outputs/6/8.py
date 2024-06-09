
def solve(n):
    # Initialize variables
    days = 0
    bacteria = 1
    split_count = 0
    
    # Loop until the total mass of the bacteria is equal to n
    while bacteria < n:
        # Increment the day count
        days += 1
        
        # Split the bacteria
        bacteria *= 2
        split_count += 1
        
        # Increment the mass of the bacteria by 1
        bacteria += 1
    
    # Return the result
    return days, split_count

