
def get_number_of_ways(N, K):
    # Initialize a 2D array to store the results
    dp = [[0] * (K + 1) for _ in range(N + 1)]
    
    # Initialize the first row with 1, because we can paint the first ball with any color
    for i in range(K + 1):
        dp[0][i] = 1
    
    # Fill the table
    for i in range(1, N + 1):
        for j in range(1, K + 1):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
    
    # Return the result for the last row
    return dp[N][K]

def main():
    N, K = map(int, input().split())
    print(get_number_of_ways(N, K))

if __name__ == '__main__':
    main()

