
def rook_placement(n, k):
    # Initialize a 2D array to store the number of ways to place rooks
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case: only one way to place a rook in the first row
    for i in range(1, n + 1):
        dp[i][1] = 1
    
    # Iterate over the remaining rows
    for i in range(2, n + 1):
        for j in range(1, n + 1):
            # Case 1: place a rook in the current row
            dp[i][j] += dp[i - 1][j]
            # Case 2: don't place a rook in the current row
            dp[i][j] += dp[i - 1][j - 1]
    
    # Return the number of ways to place rooks modulo 998244353
    return dp[n][n] % 998244353

def main():
    n, k = map(int, input().split())
    print(rook_placement(n, k))

if __name__ == '__main__':
    main()

