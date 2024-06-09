
def f1(x, y):
    # Initialize a 2D array to store the number of ways to reach each square
    dp = [[0] * (y + 1) for _ in range(x + 1)]
    
    # Initialize the number of ways to reach the origin as 1
    dp[0][0] = 1
    
    # Fill in the table
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if i == j:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 2][j - 2]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 2][j - 1] + dp[i - 1][j - 2]
    
    # Return the number of ways to reach (x, y)
    return dp[x][y] % 1000000007

def f2(x, y):
    # Initialize a 2D array to store the number of ways to reach each square
    dp = [[0] * (y + 1) for _ in range(x + 1)]
    
    # Initialize the number of ways to reach the origin as 1
    dp[0][0] = 1
    
    # Fill in the table
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if i == j:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 2][j - 2]
            else:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 2][j - 1] + dp[i - 1][j - 2]
    
    # Return the number of ways to reach (x, y)
    return dp[x][y] % 1000000007

if __name__ == '__main__':
    x, y = map(int, input().split())
    print(f1(x, y))
    print(f2(x, y))

