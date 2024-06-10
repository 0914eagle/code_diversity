
def paint_balls(n, k):
    # Initialize a 2D array to store the number of ways to paint the balls
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Initialize the first row with 1, since we can paint the first ball in any color
    for i in range(k + 1):
        dp[0][i] = 1
    
    # Fill in the table
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            # If we paint the current ball in color j, the number of ways to paint the previous balls is the same as the number of ways to paint the previous balls and the previous ball in any color
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
    
    # Return the number of ways to paint the last ball in any color
    return dp[n][k]

def main():
    n, k = map(int, input().split())
    print(paint_balls(n, k))

if __name__ == '__main__':
    main()

