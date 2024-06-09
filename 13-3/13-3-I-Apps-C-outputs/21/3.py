
def solve(n, m):
    # Initialize a list to store the positions of the chessmen
    positions = []
    # Initialize a variable to store the maximum number of chessmen
    max_chessmen = 0
    # Loop through each row
    for i in range(1, n + 1):
        # Loop through each column
        for j in range(1, m + 1):
            # Check if the current position is valid
            if valid_position(i, j, positions):
                # Add the current position to the list of positions
                positions.append((i, j))
                # Increment the maximum number of chessmen
                max_chessmen += 1
                # Recursively call the function to place the next chessman
                max_chessmen = max(max_chessmen, solve(n, m, positions))
                # Remove the current position from the list of positions
                positions.pop()
    return max_chessmen

def valid_position(i, j, positions):
    # Check if the current position is already in the list of positions
    if (i, j) in positions:
        return False
    # Loop through each position in the list of positions
    for position in positions:
        # Calculate the Manhattan distance between the current position and the position in the list
        dist = abs(i - position[0]) + abs(j - position[1])
        # Check if the Manhattan distance is less than or equal to 3
        if dist <= 3:
            return False
    return True

n, m = map(int, input().split())
print(solve(n, m))

