
def get_shortcuts():
    return {
        "R": "SrS",
        "S": "rr",
        "I": "lldll"
    }

def get_moves(grid):
    # Initialize the moves list
    moves = []
    
    # Loop through the grid and check if there are any empty spaces
    for row in grid:
        for cell in row:
            if cell == "E":
                # If there is an empty space, check if the organs can be moved
                moves += check_moves(grid, row, cell)
    
    # Return the moves list
    return moves

def check_moves(grid, row, cell):
    # Initialize the moves list
    moves = []
    
    # Check if the empty space is on the leftmost, rightmost or centermost column
    if cell in ["E", "l", "r"]:
        # If it is on the leftmost or rightmost column, check if the organ to the left or right can be moved
        if cell == "E":
            if row[row.index(cell) - 1] != "E":
                moves.append("l")
            if row[row.index(cell) + 1] != "E":
                moves.append("r")
        # If it is on the centermost column, check if the organ to the left or right can be moved
        else:
            if row[row.index(cell) - 1] != "E":
                moves.append("l")
            if row[row.index(cell) + 1] != "E":
                moves.append("r")
    
    # Return the moves list
    return moves

def get_grid(k):
    # Initialize the grid
    grid = []
    
    # Loop through the rows
    for i in range(2 * k + 1):
        # Initialize the row
        row = []
        
        # Loop through the cells
        for j in range(2 * k + 1):
            # Add the cell to the row
            row.append("E")
        
        # Add the row to the grid
        grid.append(row)
    
    # Return the grid
    return grid

def main():
    # Get the input
    k = int(input())
    
    # Get the grid
    grid = get_grid(k)
    
    # Get the moves
    moves = get_moves(grid)
    
    # Print the moves
    print(" ".join(moves))

if __name__ == '__main__':
    main()

