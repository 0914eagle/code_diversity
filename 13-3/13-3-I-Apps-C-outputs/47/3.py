
def solve(n, levels):
    # Initialize the dp table with the completion time for level 1 using item 0
    dp = [levels[0][0]]
    
    # Loop through the remaining levels
    for i in range(1, n):
        # Initialize the minimum completion time for level i using item 0
        min_time = levels[i][0]
        
        # Loop through the items available for level i
        for j in range(1, n+1):
            # If the shortcut item is available for level i
            if levels[i][1] == j:
                # Update the minimum completion time for level i using the shortcut
                min_time = min(min_time, dp[i-1] + levels[i][2])
            # Otherwise, update the minimum completion time for level i using the item
            else:
                min_time = min(min_time, dp[i-1] + levels[i][j])
        
        # Add the minimum completion time for level i to the dp table
        dp.append(min_time)
    
    # Return the minimum completion time for all levels
    return dp[-1]

