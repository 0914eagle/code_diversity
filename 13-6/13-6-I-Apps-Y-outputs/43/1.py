
def paint_balls(n, k):
    # Initialize a 2D array to store the number of ways to paint the balls
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Initialize the first row of the array with 1, because there is only one way to paint the first ball
    for i in range(k + 1):
        dp[0][i] = 1
    
    # Fill in the rest of the array using the recurrence relation
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    
    # Return the number of ways to paint the last ball
    return dp[n][k]

def main():
    n, k = map(int, input().split())
    print(paint_balls(n, k))

if __name__ == '__main__':
    main()

