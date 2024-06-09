
def f1(n, levels):
    # Initialize the dp table with the completion time for level 1
    dp = [levels[0][0]]
    
    # Loop through the remaining levels
    for i in range(1, n):
        # Get the shortcut item and completion time for the current level
        shortcut_item, completion_time = levels[i]
        
        # Initialize the minimum completion time to infinity
        min_completion_time = float('inf')
        
        # Loop through the previous levels
        for j in range(i):
            # Get the completion time for the current level using the previous level's item
            completion_time_j = dp[j] + levels[j][shortcut_item]
            
            # Update the minimum completion time
            min_completion_time = min(min_completion_time, completion_time_j)
        
        # Add the current level's completion time to the minimum completion time
        min_completion_time += completion_time
        
        # Add the minimum completion time to the dp table
        dp.append(min_completion_time)
    
    # Return the minimum completion time for all levels
    return dp[-1]

def f2(n, levels):
    # Initialize the dp table with the completion time for level 1
    dp = [levels[0][0]]
    
    # Loop through the remaining levels
    for i in range(1, n):
        # Get the shortcut item and completion time for the current level
        shortcut_item, completion_time = levels[i]
        
        # Initialize the minimum completion time to infinity
        min_completion_time = float('inf')
        
        # Loop through the previous levels
        for j in range(i):
            # Get the completion time for the current level using the previous level's item
            completion_time_j = dp[j] + levels[j][shortcut_item]
            
            # Update the minimum completion time
            min_completion_time = min(min_completion_time, completion_time_j)
        
        # Add the current level's completion time to the minimum completion time
        min_completion_time += completion_time
        
        # Add the minimum completion time to the dp table
        dp.append(min_completion_time)
    
    # Return the minimum completion time for all levels
    return dp[-1]

if __name__ == '__main__':
    n = int(input())
    levels = []
    for i in range(n):
        levels.append(list(map(int, input().split())))
    print(f1(n, levels))
    print(f2(n, levels))

