
def solve(n, levels):
    # Initialize the dp table with the completion time for level 1 using item 0
    dp = [levels[0][0]]
    
    # Loop through the remaining levels
    for i in range(1, n):
        # Initialize the minimum completion time for the current level
        min_time = float('inf')
        
        # Loop through the available items
        for j in range(n+1):
            # Check if the current item is the shortcut item for the current level
            if j == levels[i][0]:
                # If it is, the minimum completion time is the shortcut completion time
                min_time = min(min_time, levels[i][1])
            else:
                # If it's not, the minimum completion time is the completion time for the current level using the current item
                min_time = min(min_time, dp[j-1] + levels[i][j+1])
        
        # Add the minimum completion time for the current level to the dp table
        dp.append(min_time)
    
    # Return the minimum completion time for all levels
    return dp[-1]

