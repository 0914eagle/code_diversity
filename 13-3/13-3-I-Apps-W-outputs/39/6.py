
def count_tilings(N, M):
    # Initialize the dp table with all values set to 0
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: only one way to tile a table of size 1x1
    dp[1][1] = 1
    
    # Iterate over the table size
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # Count the number of ways to tile the current table
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    # Return the number of tilings modulo 10^9
    return dp[N][M] % 1000000000

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(count_tilings(N, M))

