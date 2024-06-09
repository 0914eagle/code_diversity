
def get_min_moves(n):
    # Initialize a 2D array to store the number of moves required to move all figures to a cell
    dp = [[0] * n for _ in range(n)]
    
    # Initialize a 2D array to store the number of figures in each cell
    figures = [[1] * n for _ in range(n)]
    
    # Initialize the minimum number of moves required to move all figures to a cell
    min_moves = 0
    
    # Loop through each cell in the board
    for i in range(n):
        for j in range(n):
            # If the current cell contains no figures, skip it
            if figures[i][j] == 0:
                continue
                
            # Loop through the neighboring cells of the current cell
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    # If the neighboring cell is out of the board, skip it
                    if x < 0 or x >= n or y < 0 or y >= n:
                        continue
                    
                    # If the neighboring cell contains no figures, skip it
                    if figures[x][y] == 0:
                        continue
                    
                    # If the neighboring cell is not the current cell, add the number of figures in the current cell to the number of figures in the neighboring cell
                    if (x, y) != (i, j):
                        figures[x][y] += figures[i][j]
                    
                    # If the neighboring cell is the current cell, add the number of figures in the current cell to the minimum number of moves required to move all figures to a cell
                    if (x, y) == (i, j):
                        min_moves += figures[i][j]
                    
                    # Set the number of figures in the current cell to 0
                    figures[i][j] = 0
    
    # Return the minimum number of moves required to move all figures to a cell
    return min_moves

def main():
    # Read the number of test cases
    t = int(input())
    
    # Loop through each test case
    for _ in range(t):
        # Read the size of the board
        n = int(input())
        
        # Call the get_min_moves function to find the minimum number of moves required to move all figures to a cell
        min_moves = get_min_moves(n)
        
        # Print the answer
        print(min_moves)

if __name__ == '__main__':
    main()

