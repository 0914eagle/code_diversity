
def get_min_moves(n):
    # Initialize a 2D array to store the number of moves required to get all figures to a cell
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize a 2D array to store the number of figures in each cell
    board = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize the number of figures in the first cell to 1
    board[1][1] = 1
    
    # Loop through each cell and calculate the minimum number of moves required to get all figures to that cell
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1], dp[i][j - 1], dp[i][j + 1], dp[i + 1][j - 1], dp[i + 1][j], dp[i + 1][j + 1]) + 1
    
    # Return the minimum number of moves required to get all figures to the last cell
    return dp[n][n]

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(get_min_moves(n))

if __name__ == '__main__':
    main()

