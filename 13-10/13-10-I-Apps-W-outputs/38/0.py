
def read_input():
    n, k = map(int, input().split())
    return n, k

def calculate_ways(n, k):
    # Initialize a 2D array to store the number of ways to place rooks
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Initialize the number of ways to place rooks in the first row
    for i in range(k + 1):
        dp[1][i] = 1
    
    # Fill in the table
    for i in range(2, n + 1):
        for j in range(k + 1):
            dp[i][j] = dp[i - 1][j]
            if j > 0:
                dp[i][j] += dp[i - 1][j - 1]
    
    # Return the number of ways to place rooks modulo 998244353
    return dp[n][k] % 998244353

def main():
    n, k = read_input()
    print(calculate_ways(n, k))

if __name__ == '__main__':
    main()

