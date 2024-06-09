
def count_ways(N, K):
    # Initialize a 2D array to store the results
    dp = [[0 for i in range(K+1)] for j in range(N+1)]
    
    # Initialize the first row and column with 1
    for i in range(K+1):
        dp[0][i] = 1
    for j in range(N+1):
        dp[j][0] = 1
    
    # Fill in the rest of the 2D array using the recurrence relation
    for i in range(1, N+1):
        for j in range(1, K+1):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    
    # Return the last entry of the last row
    return dp[N][K]

def main():
    N, K = map(int, input().split())
    print(count_ways(N, K))

if __name__ == '__main__':
    main()

