
def solve(C, N, M, farms, days):
    # Initialize a dictionary to store the number of farms to inspect on each day
    farms_to_inspect = {}
    
    # Iterate over each day
    for d in days:
        # Initialize a variable to store the total number of farms to inspect on this day
        total_farms = 0
        
        # Iterate over each farm with at least one cow
        for i in range(N):
            # Check if the farm has at least one cow on this day
            if farms[i] >= 1:
                # Increment the total number of farms to inspect on this day
                total_farms += 1
        
        # Add the total number of farms to inspect on this day to the dictionary
        farms_to_inspect[d] = total_farms
    
    # Return the dictionary of farms to inspect on each day
    return farms_to_inspect

