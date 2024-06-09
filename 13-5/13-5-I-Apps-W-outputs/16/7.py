
def solve(C, N, M, farms, days):
    # Initialize a dictionary to store the number of farms to inspect on each day
    farms_to_inspect = {}
    
    # Iterate over each day
    for d in days:
        # Initialize the number of farms to inspect on this day to 0
        farms_to_inspect[d] = 0
        
        # Iterate over each farm with at least one cow
        for i in range(N):
            # Get the number of cows on this farm
            c = farms[i]
            
            # If the farm has more than C cows, move half of them to a new farm
            if c > C:
                # Calculate the number of cows to move to a new farm
                num_cows_to_move = c // 2
                
                # Update the number of cows on this farm
                farms[i] = c - num_cows_to_move
                
                # Add the number of cows to move to the total number of farms to inspect on this day
                farms_to_inspect[d] += 1
    
    # Return the number of farms to inspect on each day
    return [farms_to_inspect[d] for d in days]

