
def paint_balls(n, k):
    # Initialize a 2D array to store the number of ways to paint each substring
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Initialize the first row of the 2D array with the number of ways to paint each substring of length 1
    for i in range(k + 1):
        dp[0][i] = 1
    
    # Loop through each substring of length 2 or more
    for i in range(1, n + 1):
        # Loop through each color
        for j in range(k + 1):
            # If the current color is the same as the color of the previous ball, we can't paint the current ball with this color
            if j == dp[i - 1][0]:
                dp[i][j] += dp[i - 1][1]
            # Otherwise, we can paint the current ball with any color
            else:
                dp[i][j] += dp[i - 1][j]
    
    # Return the number of ways to paint the last ball
    return dp[n][0]

def main():
    n, k = map(int, input().split())
    print(paint_balls(n, k))

if __name__ == '__main__':
    main()

