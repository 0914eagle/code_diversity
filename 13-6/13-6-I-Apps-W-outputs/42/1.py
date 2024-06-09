
def count_ways(n, k, lamps):
    # Initialize a 2D array to store the results
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Base case: when k = 0, there is only one way to choose 0 lamps
    for i in range(n + 1):
        dp[i][0] = 1
    
    # Populate the 2D array using the recurrence relation
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j == 1:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 998244353
    
    return dp[n][k]

def main():
    n, k = map(int, input().split())
    lamps = []
    for i in range(n):
        l, r = map(int, input().split())
        lamps.append((l, r))
    
    print(count_ways(n, k, lamps))

if __name__ == '__main__':
    main()

