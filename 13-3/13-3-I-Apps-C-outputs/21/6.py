
def solve(n, m):
    # Initialize a list to store the positions of the chessmen
    positions = []
    
    # Loop through each row and column
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Check if the current position is valid
            if valid_position(positions, i, j):
                # Add the current position to the list of positions
                positions.append((i, j))
    
    # Return the length of the list of positions, which is the maximum number of chessmen that can be placed
    return len(positions)

# Check if a position is valid
def valid_position(positions, i, j):
    # Loop through each existing position
    for position in positions:
        # Calculate the Manhattan distance between the current position and the existing position
        dist = abs(i - position[0]) + abs(j - position[1])
        # If the distance is less than or equal to 3, the current position is not valid
        if dist <= 3:
            return False
    
    # If all existing positions are more than 3 units away from the current position, the current position is valid
    return True

