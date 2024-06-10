
def get_tour(grid_size):
    # Initialize the grid with the given size
    grid = [[0] * grid_size[1] for _ in range(grid_size[0])]
    
    # Initialize the tour with the first square
    tour = [(0, 0)]
    
    # Loop until the entire grid is visited
    while len(tour) < grid_size[0] * grid_size[1]:
        # Get the current square
        current_square = tour[-1]
        
        # Get the possible moves from the current square
        possible_moves = get_possible_moves(current_square, grid_size)
        
        # If there are no possible moves, return -1
        if not possible_moves:
            return -1
        
        # Choose a random move from the possible moves
        move = random.choice(possible_moves)
        
        # Add the move to the tour
        tour.append(move)
        
        # Mark the moved square as visited
        grid[move[0]][move[1]] = 1
    
    # Return the tour
    return tour

def get_possible_moves(current_square, grid_size):
    # Get the current row and column
    current_row, current_col = current_square
    
    # Get the possible rows and columns
    possible_rows = [current_row - 1, current_row, current_row + 1]
    possible_cols = [current_col - 1, current_col, current_col + 1]
    
    # Filter out the impossible rows and columns
    possible_rows = [row for row in possible_rows if 0 <= row < grid_size[0]]
    possible_cols = [col for col in possible_cols if 0 <= col < grid_size[1]]
    
    # Get the possible moves
    possible_moves = [(row, col) for row in possible_rows for col in possible_cols]
    
    # Return the possible moves
    return possible_moves

if __name__ == '__main__':
    grid_size = tuple(map(int, input().split()))
    tour = get_tour(grid_size)
    if tour == -1:
        print(-1)
    else:
        for square in tour:
            print(square[0], square[1])

