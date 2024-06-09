
def count_tilings(N, M):
    # Initialize the dp table with the base case
    dp = [[0] * (M+1) for _ in range(N+1)]
    dp[0][0] = 1
    
    # Fill in the dp table
    for i in range(1, N+1):
        for j in range(1, M+1):
            # Case 1: Place a round macaron
            dp[i][j] += dp[i-1][j-1]
            # Case 2: Place an oval macaron
            dp[i][j] += dp[i-1][j-2]
    
    return dp[N][M] % 1000000007

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(count_tilings(N, M))

