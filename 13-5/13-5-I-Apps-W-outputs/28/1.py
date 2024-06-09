
def count_ways(n):
    # Initialize a 2D array to store the results
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case: when n = 1, there is only one way to fill the 3x1 tiles
    dp[1][1] = 1
    
    # Fill the table
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    
    # Return the result for the given n
    return dp[n][n]

def main():
    n = int(input())
    print(count_ways(n))

if __name__ == '__main__':
    main()

