
def f1(n, levels):
    # Initialize the dp table with the completion time for each level using item 0
    dp = [levels[i][0] for i in range(n)]

    # Loop through each level
    for i in range(1, n):
        # Loop through each item
        for j in range(1, n+1):
            # If the completion time for the current level using the current item is less than the minimum completion time so far, update the minimum completion time
            if levels[i][j] < dp[i]:
                dp[i] = levels[i][j]

    # Return the minimum completion time for all levels
    return sum(dp)

def f2(n, levels):
    # Initialize the dp table with the completion time for each level using item 0
    dp = [levels[i][0] for i in range(n)]

    # Loop through each level
    for i in range(1, n):
        # Loop through each item
        for j in range(1, n+1):
            # If the completion time for the current level using the current item is less than the minimum completion time so far, update the minimum completion time
            if levels[i][j] < dp[i]:
                dp[i] = levels[i][j]

    # Return the minimum completion time for all levels
    return sum(dp)

if __name__ == '__main__':
    n = int(input())
    levels = []
    for i in range(n):
        levels.append(list(map(int, input().split())))
    print(f1(n, levels))
    print(f2(n, levels))
