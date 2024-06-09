
def solve(n):
    # Initialize variables
    days = 0
    bacteria = 1
    split_count = 0
    
    # Loop until the total mass of the bacteria is equal to n
    while bacteria < n:
        # Increment the number of days
        days += 1
        
        # Split the bacteria
        bacteria *= 2
        
        # Increment the split count
        split_count += 1
    
    # If the total mass of the bacteria is not equal to n, return -1
    if bacteria != n:
        return -1
    
    # Return the number of days and the split count
    return days, split_count

