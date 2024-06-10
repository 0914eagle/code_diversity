
def count_ways(n, k, lamps):
    # Initialize a 2D array to store the results
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Initialize the first row and column with 1
    for i in range(n + 1):
        dp[i][0] = 1
    for j in range(k + 1):
        dp[0][j] = 0
    
    # Fill in the table
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            # If the current lamp is not turned on, then the number of ways is the same as the previous lamp
            if lamps[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            # If the current lamp is turned on, then the number of ways is the sum of the previous lamps
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 998244353
    
    # Return the result for the last lamp
    return dp[n][k]

def main():
    n, k = map(int, input().split())
    lamps = [tuple(map(int, input().split())) for _ in range(n)]
    print(count_ways(n, k, lamps))

if __name__ == '__main__':
    main()

