
def get_min_moves(n):
    # Initialize a 2D array to store the number of moves required to move all figures to a cell
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize the first row and column with 1, as we need to move the figure in the top-left cell to any other cell
    for i in range(1, n + 1):
        dp[0][i] = 1
        dp[i][0] = 1
    
    # Fill in the rest of the 2D array using the recurrence relation
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    
    # Return the answer for the bottom-right cell
    return dp[n][n]

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(get_min_moves(n))

if __name__ == '__main__':
    main()

