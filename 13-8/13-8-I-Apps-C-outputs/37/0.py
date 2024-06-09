
def get_distinct_paths(map, ship_position):
    # Initialize the number of paths to 0
    num_paths = 0
    
    # Iterate through the map
    for row in map:
        for column in row:
            # If the current cell is the ship's position, check if it can move east or west
            if column == ship_position:
                # Check if the cell to the east is a current
                if row[column+1] == ">":
                    # Increment the number of paths
                    num_paths += 1
                # Check if the cell to the west is a current
                if row[column-1] == "<":
                    # Increment the number of paths
                    num_paths += 1
    
    # Return the number of paths
    return num_paths % 1000003

