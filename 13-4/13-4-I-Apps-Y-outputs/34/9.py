
def get_min_moves(n):
    # Initialize a 2D array to store the number of moves required to move all figures to a cell
    dp = [[0] * n for _ in range(n)]
    
    # Initialize a 2D array to store the number of figures in each cell
    figures = [[0] * n for _ in range(n)]
    
    # Initialize the number of moves required to move all figures to a cell
    min_moves = 0
    
    # Loop through each cell and calculate the number of moves required to move all figures to that cell
    for i in range(n):
        for j in range(n):
            # If the current cell is not empty, calculate the number of moves required to move all figures to that cell
            if figures[i][j] > 0:
                # Calculate the number of moves required to move all figures to the cell above the current cell
                above = 0 if i == 0 else dp[i - 1][j]
                
                # Calculate the number of moves required to move all figures to the cell below the current cell
                below = 0 if i == n - 1 else dp[i + 1][j]
                
                # Calculate the number of moves required to move all figures to the cell to the left of the current cell
                left = 0 if j == 0 else dp[i][j - 1]
                
                # Calculate the number of moves required to move all figures to the cell to the right of the current cell
                right = 0 if j == n - 1 else dp[i][j + 1]
                
                # Calculate the number of moves required to move all figures to the current cell
                current = figures[i][j]
                
                # Calculate the total number of moves required to move all figures to the current cell
                total = above + below + left + right + current
                
                # Update the number of moves required to move all figures to the current cell
                dp[i][j] = total
                
                # Update the minimum number of moves required to move all figures to a cell
                min_moves = min(min_moves, total)
    
    # Return the minimum number of moves required to move all figures to a cell
    return min_moves

def main():
    # Read the number of test cases
    t = int(input())
    
    # Loop through each test case
    for _ in range(t):
        # Read the size of the board
        n = int(input())
        
        # Calculate the minimum number of moves required to move all figures to a cell
        min_moves = get_min_moves(n)
        
        # Print the minimum number of moves required to move all figures to a cell
        print(min_moves)

if __name__ == '__main__':
    main()

