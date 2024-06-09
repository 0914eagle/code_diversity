
def count_tilings(N, M):
    # Initialize the dp table with 0s
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    
    # Base case: only one way to tile a table of size 1x1
    dp[1][1] = 1
    
    # Populate the dp table
    for i in range(2, N + 1):
        for j in range(1, M + 1):
            # Count the number of ways to tile a table of size ixj with round macarons
            dp[i][j] += dp[i - 1][j - 1]
            # Count the number of ways to tile a table of size ixj with oval macarons
            dp[i][j] += dp[i - 1][j - 2]
    
    # Return the total number of tilings modulo 10^9
    return dp[N][M] % 1000000000

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(count_tilings(N, M))

