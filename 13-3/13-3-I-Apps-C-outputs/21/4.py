
def solve(n, m):
    # Initialize a list to store the positions of the chessmen
    positions = []
    # Initialize a variable to store the maximum number of chessmen
    max_chessmen = 0
    # Loop through each row
    for i in range(n):
        # Loop through each column
        for j in range(m):
            # Check if the current position is valid
            if valid_position(positions, i, j):
                # Add the current position to the list of positions
                positions.append((i, j))
                # Recursively call the function to place the next chessman
                max_chessmen = max(max_chessmen, solve(n, m, positions))
                # Remove the current position from the list of positions
                positions.pop()
    return max_chessmen

def valid_position(positions, i, j):
    # Loop through each position in the list
    for position in positions:
        # Calculate the Manhattan distance between the current position and the position in the list
        distance = abs(i - position[0]) + abs(j - position[1])
        # If the distance is less than or equal to 3, return False
        if distance <= 3:
            return False
    # If all distances are greater than 3, return True
    return True

n, m = map(int, input().split())
print(solve(n, m))

