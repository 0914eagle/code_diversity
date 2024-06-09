
def solve(n):
    # Initialize variables
    days = 0
    bacteria = 1
    splits = []
    
    # Loop until the total mass is reached
    while bacteria < n:
        # Increment the day count
        days += 1
        
        # Split the bacteria
        bacteria *= 2
        
        # Add the split to the list
        splits.append(bacteria // 2)
    
    # Check if the total mass is exactly equal to n
    if bacteria == n:
        return [days, *splits]
    else:
        return -1

