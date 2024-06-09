
def f1(n, levels):
    # Initialize the dp table
    dp = [0] * (n + 1)
    dp[0] = 0
    
    # Loop through each level
    for i in range(1, n + 1):
        # Get the completion time for the current level
        completion_time = levels[i - 1][0]
        
        # Loop through each item
        for j in range(1, n + 1):
            # Get the completion time for the current level using the current item
            current_time = levels[i - 1][j]
            
            # Check if the current time is less than the previous time
            if current_time < dp[j]:
                # Update the dp table
                dp[j] = current_time
    
    # Return the minimum time to beat all the levels
    return min(dp)

def f2(n, levels):
    # Initialize the dp table
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Loop through each level
    for i in range(1, n + 1):
        # Get the completion time for the current level
        completion_time = levels[i - 1][0]
        
        # Loop through each item
        for j in range(1, n + 1):
            # Get the completion time for the current level using the current item
            current_time = levels[i - 1][j]
            
            # Check if the current time is less than the previous time
            if current_time < dp[i - 1][j]:
                # Update the dp table
                dp[i][j] = current_time
            else:
                # Update the dp table
                dp[i][j] = dp[i - 1][j]
    
    # Return the minimum time to beat all the levels
    return min(dp[n])

if __name__ == '__main__':
    n = int(input())
    levels = []
    for i in range(n):
        levels.append(list(map(int, input().split())))
    print(f1(n, levels))
    print(f2(n, levels))

