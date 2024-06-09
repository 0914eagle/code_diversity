
def f1(n, levels):
    # Initialize the dp table with the completion time for level 1
    dp = [levels[0][0]]
    
    # Loop through the remaining levels
    for i in range(1, n):
        # Initialize the minimum completion time for the current level
        min_time = float('inf')
        
        # Loop through the items available for the current level
        for j in range(n+1):
            # If the current item is the shortcut item for the current level
            if j == levels[i][0]:
                # The minimum completion time is the completion time for the current level using the shortcut
                min_time = min(min_time, levels[i][1])
            else:
                # The minimum completion time is the minimum of the completion time for the current level using the current item and the completion time for the previous level using the current item
                min_time = min(min_time, dp[j-1] + levels[i][j+1])
        
        # Add the minimum completion time for the current level to the dp table
        dp.append(min_time)
    
    # Return the minimum completion time for all levels
    return dp[-1]

def f2(n, levels):
    # Initialize the dp table with the completion time for level 1
    dp = [levels[0][0]]
    
    # Loop through the remaining levels
    for i in range(1, n):
        # Initialize the minimum completion time for the current level
        min_time = float('inf')
        
        # Loop through the items available for the current level
        for j in range(n+1):
            # If the current item is the shortcut item for the current level
            if j == levels[i][0]:
                # The minimum completion time is the completion time for the current level using the shortcut
                min_time = min(min_time, levels[i][1])
            else:
                # The minimum completion time is the minimum of the completion time for the current level using the current item and the completion time for the previous level using the current item
                min_time = min(min_time, dp[j-1] + levels[i][j+1])
        
        # Add the minimum completion time for the current level to the dp table
        dp.append(min_time)
    
    # Return the minimum completion time for all levels
    return dp[-1]

if __name__ == '__main__':
    n = int(input())
    levels = []
    for i in range(n):
        levels.append(list(map(int, input().split())))
    print(f1(n, levels))
    print(f2(n, levels))

