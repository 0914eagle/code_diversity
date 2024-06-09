
def solve(grid):
    # Check if the grid is valid
    if not is_valid_grid(grid):
        return "SURGERY FAILED"
    
    # Initialize the empty space position
    empty_space = (0, 0)
    
    # Initialize the organs positions
    organs = {}
    for i in range(1, len(grid) + 1):
        organs[i] = (0, i)
    
    # Initialize the moves
    moves = ""
    
    # Loop until all organs are in their correct positions
    while organs != {}:
        # Find the closest organ to the empty space
        closest_organ = find_closest_organ(empty_space, organs)
        
        # Move the closest organ to the empty space
        moves += move_organ(empty_space, closest_organ, organs)
        
        # Update the empty space position
        empty_space = organs[closest_organ]
        
        # Remove the moved organ from the dictionary
        del organs[closest_organ]
    
    return "SURGERY COMPLETE\n" + moves + "\nDONE"

def is_valid_grid(grid):
    # Check if the grid is a square
    if len(grid) != len(grid[0]):
        return False
    
    # Check if the grid has a valid number of organs
    if len(grid) % 2 == 0:
        return False
    
    # Check if the grid has a single empty space
    if grid.count("E") != 1:
        return False
    
    return True

def find_closest_organ(empty_space, organs):
    # Find the organ that is closest to the empty space
    closest_distance = float("inf")
    closest_organ = -1
    for organ in organs:
        distance = manhattan_distance(empty_space, organs[organ])
        if distance < closest_distance:
            closest_distance = distance
            closest_organ = organ
    
    return closest_organ

def manhattan_distance(position1, position2):
    # Calculate the Manhattan distance between two positions
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])

def move_organ(empty_space, organ, organs):
    # Move the organ to the empty space
    organs[organ] = empty_space
    return "l" if empty_space[1] < organ else "r"

