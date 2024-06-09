
def count_polygons(R, C):
    # Initialize a 2D array to store the number of polygons for each cell
    dp = [[0] * (C + 1) for _ in range(R + 1)]

    # Initialize the first row and column with 1, since we can form a polygon with a single chocolate
    for i in range(C + 1):
        dp[0][i] = 1
    for i in range(R + 1):
        dp[i][0] = 1

    # Fill in the rest of the 2D array using the recurrence relation
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[R][C]

if __name__ == '__main__':
    R, C = map(int, input().split())
    print(count_polygons(R, C))

