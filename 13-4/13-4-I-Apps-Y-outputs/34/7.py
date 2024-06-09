
def f1(n):
    # Initialize the board with the given size
    board = [[0] * n for _ in range(n)]
    
    # Initialize the number of moves to 0
    moves = 0
    
    # Initialize the number of figures to move
    num_figures = n * n
    
    # Initialize the current cell to move the figures from
    current_cell = (0, 0)
    
    # Initialize the target cell to move the figures to
    target_cell = (n - 1, n - 1)
    
    # While there are still figures to move
    while num_figures > 0:
        # Get the current figure from the current cell
        current_figure = board[current_cell[0]][current_cell[1]]
        
        # If the current figure is not 0 (i.e. there is a figure in the current cell)
        if current_figure != 0:
            # Move the figure to the target cell
            board[target_cell[0]][target_cell[1]] += current_figure
            
            # Set the current cell to the target cell
            current_cell = target_cell
            
            # Decrement the number of figures to move
            num_figures -= 1
            
        # Increment the number of moves
        moves += 1
        
        # If the current cell is not the last cell (i.e. there are still cells to move the figures to)
        if current_cell != (n - 1, n - 1):
            # Get the next cell to move the figures to
            target_cell = get_next_cell(current_cell, n)
    
    # Return the minimum number of moves needed to get all the figures into one cell
    return moves

def get_next_cell(current_cell, n):
    # Get the next cell to move the figures to
    next_cell = (current_cell[0] - 1, current_cell[1] - 1)
    
    # If the next cell is out of the board, get the next cell to the right
    if next_cell[0] < 0 or next_cell[1] < 0:
        next_cell = (current_cell[0], current_cell[1] + 1)
    
    # If the next cell is out of the board, get the next cell to the bottom
    if next_cell[0] >= n or next_cell[1] >= n:
        next_cell = (current_cell[0] + 1, current_cell[1])
    
    # If the next cell is out of the board, get the next cell to the left
    if next_cell[0] < 0 or next_cell[1] < 0:
        next_cell = (current_cell[0], current_cell[1] - 1)
    
    # If the next cell is out of the board, get the next cell to the top
    if next_cell[0] >= n or next_cell[1] >= n:
        next_cell = (current_cell[0] - 1, current_cell[1])
    
    # Return the next cell to move the figures to
    return next_cell

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(f1(n))

