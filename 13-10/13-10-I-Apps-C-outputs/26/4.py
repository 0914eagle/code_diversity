
def find_tour(grid):
    # Initialize a dictionary to store the visited squares
    visited = {}
    
    # Initialize the starting square
    current_square = (0, 0)
    
    # Initialize the tour
    tour = []
    
    # Loop until all squares are visited
    while len(visited) < len(grid) * len(grid[0]):
        # Get the current square's coordinates
        current_row, current_col = current_square
        
        # Get the next square's coordinates based on the Manhattan distance constraint
        next_row, next_col = current_row + 1, current_col + 1
        if next_row == len(grid):
            next_row = 0
        if next_col == len(grid[0]):
            next_col = 0
        
        # Add the next square to the tour
        tour.append((next_row, next_col))
        
        # Mark the next square as visited
        visited[(next_row, next_col)] = True
        
        # Update the current square
        current_square = (next_row, next_col)
    
    # Return the tour
    return tour

def main():
    # Read the input
    grid_size = input().split()
    N, M = int(grid_size[0]), int(grid_size[1])
    grid = []
    for i in range(N):
        grid.append(input().split())
    
    # Find the tour
    tour = find_tour(grid)
    
    # Print the tour
    for square in tour:
        print(square[0], square[1])

if __name__ == '__main__':
    main()

