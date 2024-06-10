
def get_num_ways(n, k):
    # Initialize a 2D array to store the number of ways to paint the balls
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Base case: only one way to paint the first ball
    dp[1][0] = 1
    
    # Populate the table
    for i in range(2, n + 1):
        for j in range(1, k + 1):
            # The number of ways to paint the current ball is the sum of the number of ways to paint the previous ball with each color
            dp[i][j] = sum(dp[i - 1][:j]) + sum(dp[i - 1][j:])
    
    # Return the number of ways to paint all the balls
    return dp[n][k]

def main():
    n, k = map(int, input().split())
    print(get_num_ways(n, k))

if __name__ == '__main__':
    main()

