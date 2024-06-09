
def f1(n, levels):
    # Initialize the dp array with the completion time for level 1
    dp = [levels[0][-1]]
    
    # Loop through the remaining levels
    for i in range(1, n):
        # Get the shortcut item and completion time for the current level
        shortcut_item, completion_time = levels[i][:2]
        
        # Initialize the minimum completion time to infinity
        min_completion_time = float('inf')
        
        # Loop through the items available for the current level
        for j in range(n+1):
            # If the current item is the shortcut item, set the completion time to the shortcut completion time
            if j == shortcut_item:
                completion_time = levels[i][-1]
            
            # Get the completion time for the current level using the current item
            current_completion_time = levels[i][j]
            
            # If the current completion time is less than the minimum completion time, update the minimum completion time
            if current_completion_time < min_completion_time:
                min_completion_time = current_completion_time
        
        # Add the minimum completion time for the current level to the dp array
        dp.append(dp[i-1] + min_completion_time)
    
    # Return the minimum completion time for all levels
    return dp[-1]

def f2(n, levels):
    # Initialize the dp array with the completion time for level 1
    dp = [levels[0][-1]]
    
    # Loop through the remaining levels
    for i in range(1, n):
        # Get the shortcut item and completion time for the current level
        shortcut_item, completion_time = levels[i][:2]
        
        # Initialize the minimum completion time to infinity
        min_completion_time = float('inf')
        
        # Loop through the items available for the current level
        for j in range(n+1):
            # If the current item is the shortcut item, set the completion time to the shortcut completion time
            if j == shortcut_item:
                completion_time = levels[i][-1]
            
            # Get the completion time for the current level using the current item
            current_completion_time = levels[i][j]
            
            # If the current completion time is less than the minimum completion time, update the minimum completion time
            if current_completion_time < min_completion_time:
                min_completion_time = current_completion_time
        
        # Add the minimum completion time for the current level to the dp array
        dp.append(dp[i-1] + min_completion_time)
    
    # Return the minimum completion time for all levels
    return dp[-1]

if __name__ == '__main__':
    n = int(input())
    levels = []
    for i in range(n):
        levels.append(list(map(int, input().split())))
    print(f1(n, levels))
    print(f2(n, levels))

