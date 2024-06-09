
def get_suitable_colorings(n, k):
    # Initialize a 2D array to store the number of suitable colorings for each cell
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case: Only one cell
    dp[1][1] = 2
    
    # Base case: Only two cells
    dp[2][2] = 6
    
    for i in range(3, n + 1):
        for j in range(1, n + 1):
            # If j is greater than k, then no rectangle of a single color can be formed
            if j > k:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % 998244353
            # If j is less than or equal to k, then a rectangle of a single color can be formed
            else:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 2][j - 1]) % 998244353
    
    return dp[n][n]

def main():
    n, k = map(int, input().split())
    print(get_suitable_colorings(n, k))

if __name__ == '__main__':
    main()

