
def get_num_ways(a, b, c):
    # Initialize a 2D array to store the number of ways to reach each island
    dp = [[0] * (c + 1) for _ in range(a + 1)]
    
    # Base case: when there are no islands, there is only one way to reach it
    for i in range(a + 1):
        dp[i][0] = 1
    
    # Populate the 2D array using the recurrence relation
    for i in range(1, a + 1):
        for j in range(1, c + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    # Return the number of ways to reach the red cluster modulo 998244353
    return dp[a][c] % 998244353

def main():
    a, b, c = map(int, input().split())
    print(get_num_ways(a, b, c))

if __name__ == '__main__':
    main()

