
import sys

def number_of_ways_to_place_rooks(n, k):
    # Initialize a 2D array to store the number of ways to place rooks
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    # Base case: when n = 1, there is only one way to place a rook
    dp[1][0] = 1
    
    for i in range(2, n + 1):
        for j in range(k + 1):
            # Count the number of ways to place rooks in the ith row
            dp[i][j] += dp[i - 1][j]
            if j > 0:
                # Count the number of ways to place rooks in the ith row and attack j pairs of rooks
                dp[i][j] += dp[i - 1][j - 1]
    
    return dp[n][k]

def main():
    n, k = map(int, sys.stdin.readline().split())
    print(number_of_ways_to_place_rooks(n, k) % 998244353)

if __name__ == '__main__':
    main()

