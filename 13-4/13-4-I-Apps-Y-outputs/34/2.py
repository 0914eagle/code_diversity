
def get_min_moves(n):
    # Initialize a 2D array to store the number of moves required to move all figures to a cell
    dp = [[0] * n for _ in range(n)]
    
    # Initialize a queue to store the cells to be processed
    queue = [(0, 0)]
    
    # Loop until the queue is empty
    while queue:
        # Get the current cell from the queue
        i, j = queue.pop(0)
        
        # Check if the current cell is the target cell (i.e. (n-1, n-1))
        if i == n-1 and j == n-1:
            # If it is the target cell, return the number of moves required to get there
            return dp[i][j]
        
        # Loop through all the neighboring cells
        for ii, jj in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
            # Check if the neighboring cell is valid (i.e. inside the board)
            if 0 <= ii < n and 0 <= jj < n:
                # If the neighboring cell is valid, check if the number of moves required to move all figures to that cell is less than the current number of moves
                if dp[ii][jj] > dp[i][j] + 1:
                    # If it is, update the number of moves required to move all figures to that cell and add the cell to the queue
                    dp[ii][jj] = dp[i][j] + 1
                    queue.append((ii, jj))
    
    # If the target cell is not reached, return -1
    return -1

def main():
    # Read the number of test cases
    t = int(input())
    
    # Loop through each test case
    for _ in range(t):
        # Read the size of the board
        n = int(input())
        
        # Call the get_min_moves function to get the minimum number of moves required to move all figures to a cell
        print(get_min_moves(n))

if __name__ == '__main__':
    main()

