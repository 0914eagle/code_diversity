
def solve(grid):
    # Check if the grid is valid
    if not is_valid_grid(grid):
        return "SURGERY FAILED"
    
    # Initialize the empty space coordinates
    empty_space = find_empty_space(grid)
    
    # Initialize the organs coordinates
    organs = find_organs(grid)
    
    # Initialize the sequence of moves
    sequence = ""
    
    # Loop through the organs and move them to their correct position
    for organ in organs:
        # Check if the organ is in its correct position
        if organ == empty_space:
            continue
        
        # Move the organ to the empty space
        sequence += move_organ(organ, empty_space)
        
        # Update the empty space coordinates
        empty_space = find_empty_space(grid)
    
    # Check if all organs are in their correct position
    if all(organ == empty_space for organ in organs):
        return "SURGERY COMPLETE\n" + sequence
    else:
        return "SURGERY FAILED"

def is_valid_grid(grid):
    # Check if the grid is a square
    if len(grid) != len(grid[0]):
        return False
    
    # Check if the grid has an even number of rows and columns
    if len(grid) % 2 != 0:
        return False
    
    # Check if the grid has the correct number of organs
    if len(grid) * len(grid[0]) != 4 * (len(grid) // 2):
        return False
    
    # Check if the grid has exactly one empty space
    if grid.count("E") != 1:
        return False
    
    return True

def find_empty_space(grid):
    for row in grid:
        for col in row:
            if col == "E":
                return (row.index(col), col)

def find_organs(grid):
    organs = []
    for row in grid:
        for col in row:
            if col != "E":
                organs.append((row.index(col), col))
    return organs

def move_organ(organ, empty_space):
    # Check if the organ is in the top row
    if organ[0] == 0:
        # Move the organ down
        return "d"
    # Check if the organ is in the bottom row
    elif organ[0] == len(grid) - 1:
        # Move the organ up
        return "u"
    # Check if the organ is in the leftmost column
    elif organ[1] == 0:
        # Move the organ to the right
        return "r"
    # Check if the organ is in the rightmost column
    elif organ[1] == len(grid[0]) - 1:
        # Move the organ to the left
        return "l"
    # Check if the organ is in the center column
    else:
        # Move the organ to the left or to the right
        return "l" if organ[1] > empty_space[1] else "r"

if __name__ == '__main__':
    grid = [
        [1, 2, 3, 5, 6, "E", 7],
        [8, 9, 10, 4, 11, 12, 13]
    ]
    print(solve(grid))

