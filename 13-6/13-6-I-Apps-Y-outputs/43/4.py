
def number_of_ways_to_paint_balls(n, k):
    # Initialize a 2D array to store the results
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Initialize the first row with 1, because we can paint the first ball with any color
    for i in range(k + 1):
        dp[0][i] = 1
    
    # Fill in the table
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    
    # Return the result for the last ball and the last color
    return dp[n][k]

def main():
    n, k = map(int, input().split())
    print(number_of_ways_to_paint_balls(n, k))

if __name__ == '__main__':
    main()

