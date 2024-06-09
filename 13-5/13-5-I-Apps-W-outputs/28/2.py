
def count_ways(n):
    # Initialize a 2D array to store the results
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize the first row and column with 1
    for i in range(n + 1):
        dp[i][0] = 1
        dp[0][i] = 1
    
    # Fill the 2D array using the recurrence relation
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    # Return the result for the last cell
    return dp[n][n]

def main():
    n = int(input())
    print(count_ways(n))

if __name__ == '__main__':
    main()

