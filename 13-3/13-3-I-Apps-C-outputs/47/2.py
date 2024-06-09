
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
                # If so, the minimum completion time is the completion time for the level using the shortcut
                min_time = min(min_time, levels[i][1])
            else:
                # If not, the minimum completion time is the maximum of the completion time for the level using the current item and the previous level's completion time using the current item
                min_time = max(min_time, levels[i][j+1] + dp[j])
        
        # Add the minimum completion time for the current level to the dp table
        dp.append(min_time)
    
    # Return the total completion time for all levels
    return sum(dp)

