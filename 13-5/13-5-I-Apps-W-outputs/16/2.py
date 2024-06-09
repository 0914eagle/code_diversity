
def solve(C, N, M, cows, days):
    # Initialize a dictionary to store the number of farms visited on each day
    farms_visited = {}
    
    # Loop through each day
    for d in days:
        # Initialize the number of farms visited on this day to 0
        farms_visited[d] = 0
        
        # Loop through each farm with at least one cow
        for i in range(N):
            # If the farm has more than C cows, move half of them to a new farm
            if cows[i] > C:
                cows[i] = int(cows[i] / 2)
                cows.append(int(cows[i] / 2))
            
            # Increment the number of farms visited on this day
            farms_visited[d] += 1
    
    # Return the number of farms visited on each day
    return [farms_visited[d] for d in days]

