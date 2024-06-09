
def count_ways(N, M, conditions):
    # Initialize a 2D array to store the number of ways to paint each square
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    
    # Initialize the first row and column of the array
    for i in range(N + 1):
        dp[0][i] = 1
    for i in range(M + 1):
        dp[i][0] = 1
    
    # Fill in the rest of the array using the recurrence relation
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            dp[i][j] = (dp[i - 1][j - 1] * (conditions[i - 1][2] - 1) + dp[i - 1][j] * (conditions[i - 1][2] - 1)) % 1000000007
    
    # Return the number of ways to paint the last square
    return dp[M][N]

def main():
    N, M = map(int, input().split())
    conditions = []
    for _ in range(M):
        l, r, x = map(int, input().split())
        conditions.append([l, r, x])
    print(count_ways(N, M, conditions))

if __name__ == '__main__':
    main()

