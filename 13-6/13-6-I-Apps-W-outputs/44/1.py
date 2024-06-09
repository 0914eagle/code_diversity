
import sys

def get_beautiful_colorings(n, k):
    # Base case: If n is 1, return 1
    if n == 1:
        return 1
    
    # Initialize a 2D array to store the results
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize the first row and column with 1
    for i in range(n + 1):
        dp[0][i] = 1
        dp[i][0] = 1
    
    # Fill in the table
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 998244353
    
    # Return the result
    return dp[n][n]

def get_suitable_colorings(n, k):
    # Get the number of beautiful colorings
    beautiful_colorings = get_beautiful_colorings(n, k)
    
    # Initialize a 2D array to store the results
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize the first row and column with 1
    for i in range(n + 1):
        dp[0][i] = 1
        dp[i][0] = 1
    
    # Fill in the table
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 998244353
    
    # Return the result
    return (dp[n][n] - beautiful_colorings + 998244353) % 998244353

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(get_suitable_colorings(n, k))

