
def get_number_of_ways_to_paint_balls(n, k):
    # Initialize a 2D array to store the number of ways to paint the balls
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Initialize the first row of the 2D array with 1, since there is only one way to paint the first ball
    for i in range(k + 1):
        dp[0][i] = 1
    
    # Iterate over the remaining balls
    for i in range(1, n + 1):
        # Iterate over the available colors
        for j in range(k + 1):
            # Calculate the number of ways to paint the current ball
            dp[i][j] = sum(dp[i - 1][:j]) + sum(dp[i - 1][j:])
    
    # Return the number of ways to paint the last ball
    return dp[n][-1]

def main():
    n, k = map(int, input().split())
    print(get_number_of_ways_to_paint_balls(n, k))

if __name__ == '__main__':
    main()

