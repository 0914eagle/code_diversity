
def input_data():
    n, k = map(int, input().split())
    return n, k

def rook_placement(n, k):
    # Initialize a 2D array to store the number of ways to place rooks
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case: If n is 1, there is only one way to place a rook
    dp[1][1] = 1
    
    # Iterate over the rows
    for i in range(2, n + 1):
        # Iterate over the columns
        for j in range(1, n + 1):
            # If the cell is empty, add the number of ways to place a rook in the previous row and column
            if j > 1:
                dp[i][j] += dp[i - 1][j - 1]
            # Add the number of ways to place a rook in the previous row
            dp[i][j] += dp[i - 1][j]
            # Add the number of ways to place a rook in the previous column
            dp[i][j] += dp[i][j - 1]
    
    # Return the number of ways to place rooks modulo 998244353
    return dp[n][n] % 998244353

def main():
    n, k = input_data()
    print(rook_placement(n, k))

if __name__ == '__main__':
    main()

