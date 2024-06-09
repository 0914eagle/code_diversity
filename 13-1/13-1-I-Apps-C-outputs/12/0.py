
def f1(n, levels):
    # Initialize the dp table with the completion time for level 1
    dp = [levels[0][0]]
    for i in range(1, n):
        # Initialize the minimum completion time for level i
        min_time = float('inf')
        for j in range(n+1):
            # Calculate the completion time for level i using item j
            time = dp[j-1] + levels[i][j]
            # Update the minimum completion time for level i
            min_time = min(min_time, time)
        # Add the minimum completion time for level i to the dp table
        dp.append(min_time)
    # Return the minimum completion time for all levels
    return dp[-1]

def f2(n, levels):
    # Initialize the dp table with the completion time for level 1
    dp = [levels[0][0]]
    for i in range(1, n):
        # Initialize the minimum completion time for level i
        min_time = float('inf')
        for j in range(n+1):
            # Calculate the completion time for level i using item j
            time = dp[j-1] + levels[i][j]
            # Update the minimum completion time for level i
            min_time = min(min_time, time)
        # Add the minimum completion time for level i to the dp table
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

