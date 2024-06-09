
def get_max_chessmen(n, m):
    # Initialize a list to store the positions of the chessmen
    positions = []
    # Initialize a variable to store the maximum number of chessmen
    max_chessmen = 0
    # Loop through each row
    for i in range(n):
        # Loop through each column
        for j in range(m):
            # Check if the current position is valid
            if is_valid_position(positions, i, j):
                # Add the current position to the list of positions
                positions.append((i, j))
                # Recursively call the function to place the next chessman
                max_chessmen = max(max_chessmen, 1 + get_max_chessmen(n, m))
                # Remove the current position from the list of positions
                positions.pop()
    return max_chessmen

def is_valid_position(positions, i, j):
    # Loop through each existing position
    for position in positions:
        # Calculate the Manhattan distance between the current position and the existing position
        dist = abs(i - position[0]) + abs(j - position[1])
        # If the Manhattan distance is less than or equal to 3, the current position is not valid
        if dist <= 3:
            return False
    return True

n, m = map(int, input().split())
print(get_max_chessmen(n, m))

