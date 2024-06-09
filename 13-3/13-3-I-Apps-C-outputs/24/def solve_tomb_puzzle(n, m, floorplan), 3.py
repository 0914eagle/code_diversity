
def solve_tomb_puzzle(n, m, floorplan):
    # Initialize a list to store the gargoyle positions
    gargoyle_positions = []
    
    # Loop through each row of the floorplan
    for i in range(n):
        # Loop through each column of the floorplan
        for j in range(m):
            # If the current cell is a gargoyle, add its position to the list
            if floorplan[i][j] in ["V", "H"]:
                gargoyle_positions.append((i, j))
    
    # Initialize a variable to store the minimum number of gargoyles that need to be rotated
    min_rotations = float("inf")
    
    # Loop through each possible rotation of the gargoyles
    for rotation in range(4):
        # Initialize a variable to store the number of gargoyles that are visible from each other
        num_visible_gargoyles = 0
        
        # Loop through each gargoyle position
        for i in range(len(gargoyle_positions)):
            # Get the current gargoyle position
            gargoyle_position = gargoyle_positions[i]
            
            # Loop through each other gargoyle position
            for j in range(i+1, len(gargoyle_positions)):
                # Get the other gargoyle position
                other_gargoyle_position = gargoyle_positions[j]
                
                # Check if the two gargoyles are visible from each other
                if are_gargoyles_visible(gargoyle_position, other_gargoyle_position, floorplan, rotation):
                    num_visible_gargoyles += 1
        
        # If the number of visible gargoyles is equal to the number of gargoyles, we have found a solution
        if num_visible_gargoyles == len(gargoyle_positions):
            return rotation
        
        # If the number of visible gargoyles is less than the minimum number of gargoyles that need to be rotated, update the minimum number of gargoyles that need to be rotated
        if num_visible_gargoyles < min_rotations:
            min_rotations = num_visible_gargoyles
    
    # If no solution is found, return -1
    return -1

# Check if two gargoyles are visible from each other
def are_gargoyles_visible(gargoyle_position, other_gargoyle_position, floorplan, rotation):
    # Get the x and y coordinates of the gargoyles
    x1, y1 = gargoyle_position
    x2, y2 = other_gargoyle_position
    
    # Check if the gargoyles are in the same row or column
    if x1 == x2 or y1 == y2:
        return True
    
    # Check if the gargoyles are diagonal from each other
    if abs(x1 - x2) == abs(y1 - y2):
        # Check if the gargoyles are facing each other
        if rotation % 2 == 0:
            return True
        else:
            return False
    
    # If the gargoyles are not in the same row, column, or diagonal, they are not visible from each other
    return False

