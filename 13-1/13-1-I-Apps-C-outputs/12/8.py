
def f1(n, levels):
    # Initialize the dp table with the completion time for level 1
    dp = [levels[0][0]]
    for i in range(1, n):
        # Find the minimum completion time for level i using all the items
        min_time = float('inf')
        for j in range(n+1):
            min_time = min(min_time, dp[j-1] + levels[i][j])
        # Add the shortcut completion time for level i
        min_time = min(min_time, levels[i][0] + dp[n])
        dp.append(min_time)
    return dp[-1]

def f2(n, levels):
    # Initialize the dp table with the completion time for level 1
    dp = [levels[0][0]]
    for i in range(1, n):
        # Find the minimum completion time for level i using all the items
        min_time = float('inf')
        for j in range(n+1):
            min_time = min(min_time, dp[j-1] + levels[i][j])
        # Add the shortcut completion time for level i
        min_time = min(min_time, levels[i][0] + dp[n])
        dp.append(min_time)
    return dp[-1]

if __name__ == '__main__':
    n = int(input())
    levels = []
    for i in range(n):
        levels.append(list(map(int, input().split())))
    print(f1(n, levels))
    print(f2(n, levels))

