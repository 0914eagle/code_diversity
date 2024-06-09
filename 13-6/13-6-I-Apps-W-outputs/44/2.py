
import itertools

def count_suitable_colorings(n, k):
    # Initialize a 2D array to store the number of ways to color each cell
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize the first row and column with 1 way to color each cell
    for i in range(n + 1):
        dp[i][0] = 1
        dp[0][i] = 1
    
    # Fill in the rest of the 2D array using the recurrence relation
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 998244353
    
    # Return the number of ways to color the board
    return dp[n][n]

def main():
    n, k = map(int, input().split())
    print(count_suitable_colorings(n, k))

if __name__ == '__main__':
    main()

