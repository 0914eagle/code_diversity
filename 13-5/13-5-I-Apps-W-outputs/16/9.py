
def solve(C, N, M, cows, days):
    # Initialize a dictionary to store the number of farms to inspect on each day
    farms_to_inspect = {}
    
    # Iterate over each day
    for d in days:
        # Initialize a variable to store the total number of farms to inspect on this day
        total_farms = 0
        
        # Iterate over each farm with at least one cow
        for i in range(N):
            # Check if the farm has more than C cows on this day
            if cows[i] > C:
                # Calculate the number of cows that will be moved to a new farm
                num_cows_to_move = cows[i] // 2
                
                # Add the number of cows that will be moved to the total number of farms to inspect on this day
                total_farms += num_cows_to_move
        
        # Add the total number of farms to inspect on this day to the dictionary
        farms_to_inspect[d] = total_farms
    
    return farms_to_inspect

