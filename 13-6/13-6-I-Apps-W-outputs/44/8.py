
def get_number_of_suitable_colorings(n, k):
    # Initialize a 2D array to store the number of ways to color each cell
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case: only one cell
    dp[1][1] = 2
    
    # Base case: only two cells
    dp[2][2] = 6
    
    for i in range(3, n + 1):
        for j in range(1, n + 1):
            # If j is greater than k, then there is no need to consider this cell
            if j > k:
                break
            # If j is 1, then the cell can be colored either black or white
            if j == 1:
                dp[i][j] = 2
            # If j is greater than 1, then the cell can be colored either black or white,
            # and the previous cell can be colored either black or white as well
            else:
                dp[i][j] = dp[i - 1][j - 1] * 2 + dp[i - 1][j]
    
    # Return the number of suitable colorings modulo 998244353
    return dp[n][k] % 998244353

def main():
    n, k = map(int, input().split())
    print(get_number_of_suitable_colorings(n, k))

if __name__ == '__main__':
    main()

