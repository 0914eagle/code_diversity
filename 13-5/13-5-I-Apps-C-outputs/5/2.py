
def f1(n, levels):
    # Initialize the dp table with the completion time for level 1 using item 0
    dp = [levels[0][0]]
    
    # Loop through the remaining levels
    for i in range(1, n):
        # Initialize the minimum completion time for level i using item 0
        min_time = levels[i][0]
        
        # Loop through the items 1 to n
        for j in range(1, n+1):
            # If the shortcut item for level i is item j, add the completion time for level i using item j to the minimum completion time
            if levels[i][1] == j:
                min_time += levels[i][j+1]
                break
            # Otherwise, if the completion time for level i using item j is less than the minimum completion time, update the minimum completion time
            elif levels[i][j+1] < min_time:
                min_time = levels[i][j+1]
        
        # Add the minimum completion time for level i to the dp table
        dp.append(min_time)
    
    # Return the sum of the dp table
    return sum(dp)

def f2(n, levels):
    # Initialize the dp table with the completion time for level 1 using item 0
    dp = [levels[0][0]]
    
    # Loop through the remaining levels
    for i in range(1, n):
        # Initialize the minimum completion time for level i using item 0
        min_time = levels[i][0]
        
        # Loop through the items 1 to n
        for j in range(1, n+1):
            # If the completion time for level i using item j is less than the minimum completion time, update the minimum completion time
            if levels[i][j+1] < min_time:
                min_time = levels[i][j+1]
        
        # Add the minimum completion time for level i to the dp table
        dp.append(min_time)
    
    # Return the sum of the dp table
    return sum(dp)

if __name__ == '__main__':
    n = int(input())
    levels = []
    for i in range(n):
        levels.append(list(map(int, input().split())))
    print(f1(n, levels))
    print(f2(n, levels))

