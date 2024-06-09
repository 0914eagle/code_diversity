
def get_min_moves(n):
    # Initialize a 2D array to store the number of moves required to move all figures to a cell
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize a 2D array to store the number of figures in each cell
    figures = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize the number of moves required to move all figures to a cell
    dp[1][1] = 1
    
    # Loop through each cell
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # If the current cell contains a figure, add it to the number of figures in the cell
            if figures[i][j] > 0:
                figures[i][j] += 1
            
            # Loop through all the cells that can be reached from the current cell
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    # If the current cell is not the starting cell and the cell being reached is within the bounds of the board
                    if (i, j) != (1, 1) and 1 <= i + di <= n and 1 <= j + dj <= n:
                        # Add the number of moves required to move the figure from the current cell to the cell being reached
                        dp[i + di][j + dj] += dp[i][j]
    
    # Return the minimum number of moves required to move all figures to a cell
    return min(dp[n][n])

def main():
    # Read the number of test cases
    t = int(input())
    
    # Loop through each test case
    for _ in range(t):
        # Read the size of the board
        n = int(input())
        
        # Print the minimum number of moves required to move all figures to a cell
        print(get_min_moves(n))

if __name__ == '__main__':
    main()

