
def f1(n, levels):
    # Initialize the dp array with the completion time for level 1
    dp = [levels[0][0]]
    
    # Loop through the remaining levels
    for i in range(1, n):
        # Get the shortcut item and completion time for the current level
        shortcut_item, shortcut_time = levels[i][:2]
        
        # Initialize the minimum completion time to infinity
        min_time = float('inf')
        
        # Loop through the previous levels
        for j in range(i):
            # Get the completion time for the current level using the previous level's item
            time = dp[j] + levels[i][j + 2]
            
            # If the completion time is less than the minimum, update the minimum
            if time < min_time:
                min_time = time
        
        # If the shortcut item is not the same as the previous level's item,
        # add the shortcut completion time to the minimum
        if shortcut_item != i:
            min_time += shortcut_time
        
        # Add the minimum completion time to the dp array
        dp.append(min_time)
    
    # Return the minimum completion time for all levels
    return dp[-1]

def f2(n, levels):
    # Initialize the dp array with the completion time for level 1
    dp = [levels[0][0]]
    
    # Loop through the remaining levels
    for i in range(1, n):
        # Get the shortcut item and completion time for the current level
        shortcut_item, shortcut_time = levels[i][:2]
        
        # Initialize the minimum completion time to infinity
        min_time = float('inf')
        
        # Loop through the previous levels
        for j in range(i):
            # Get the completion time for the current level using the previous level's item
            time = dp[j] + levels[i][j + 2]
            
            # If the completion time is less than the minimum, update the minimum
            if time < min_time:
                min_time = time
        
        # If the shortcut item is not the same as the previous level's item,
        # add the shortcut completion time to the minimum
        if shortcut_item != i:
            min_time += shortcut_time
        
        # Add the minimum completion time to the dp array
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

