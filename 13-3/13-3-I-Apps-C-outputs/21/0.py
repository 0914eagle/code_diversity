
def max_chessmen(n, m):
    # Initialize a list to store the positions of the chessmen
    positions = []
    # Initialize a variable to store the maximum number of chessmen
    max_chessmen = 0
    # Loop through each row
    for i in range(n):
        # Loop through each column
        for j in range(m):
            # Check if the current position is valid
            if valid_position(i, j, positions):
                # Add the current position to the list of positions
                positions.append((i, j))
                # Recursively call the function to place the next chessmen
                max_chessmen = max(max_chessmen, place_chessmen(n, m, positions))
                # Remove the current position from the list of positions
                positions.pop()
    return max_chessmen

def valid_position(i, j, positions):
    # Check if the current position is already in the list of positions
    if (i, j) in positions:
        return False
    # Loop through each position in the list of positions
    for position in positions:
        # Calculate the Manhattan distance between the current position and the position in the list of positions
        distance = abs(i - position[0]) + abs(j - position[1])
        # Check if the Manhattan distance is less than or equal to 3
        if distance <= 3:
            return False
    return True

def place_chessmen(n, m, positions):
    # If all positions have been placed, return the number of chessmen placed
    if len(positions) == n * m:
        return len(positions)
    # Initialize a variable to store the maximum number of chessmen placed
    max_chessmen = 0
    # Loop through each row
    for i in range(n):
        # Loop through each column
        for j in range(m):
            # Check if the current position is valid
            if valid_position(i, j, positions):
                # Add the current position to the list of positions
                positions.append((i, j))
                # Recursively call the function to place the next chessmen
                max_chessmen = max(max_chessmen, place_chessmen(n, m, positions))
                # Remove the current position from the list of positions
                positions.pop()
    return max_chessmen

n, m = map(int, input().split())
print(max_chessmen(n, m))

