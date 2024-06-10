
def place_rooks(n, k):
    # Initialize a 2D array to store the number of ways to place rooks
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base case: when n = 1, there is only one way to place one rook
    dp[1][1] = 1
    
    # Loop through all possible rows and columns
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # When k = 0, any placement is valid
            if k == 0:
                dp[i][j] = 1
            # When k > 0, we need to consider the previous placements
            else:
                # Loop through the previous rows and columns
                for x in range(1, i):
                    for y in range(1, j):
                        # If the previous placement is valid, add the number of ways to place the current rook
                        if dp[x][y] > 0:
                            dp[i][j] = (dp[i][j] + dp[x][y]) % 998244353
    
    # Return the number of ways to place the rooks
    return dp[n][n]

def main():
    n, k = map(int, input().split())
    print(place_rooks(n, k))

if __name__ == '__main__':
    main()

