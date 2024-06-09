
def count_tilings(N, M):
    # Initialize the dp array with 0s
    dp = [0] * (M + 1)
    
    # Base case: only one way to tile a table of size 1x1
    dp[1] = 1
    
    for i in range(2, M + 1):
        # Count the number of ways to tile a table of size 1xi with round macarons
        dp[i] += dp[i - 1]
        
        # Count the number of ways to tile a table of size 1xi with oval macarons
        dp[i] += dp[i - 2]
    
    # Return the total number of tilings modulo 10^9
    return dp[M] % 1000000000

if __name__ == '__main__':
    N, M = map(int, input().split())
    print(count_tilings(N, M))

