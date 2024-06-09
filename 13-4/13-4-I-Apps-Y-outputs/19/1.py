
def get_max_distance(grid):
    # Initialize the maximum distance to 0
    max_distance = 0
    
    # Loop through each row of the grid
    for i in range(len(grid)):
        # Loop through each column of the grid
        for j in range(len(grid[0])):
            # If the current block is a spy
            if grid[i][j] == "S":
                # Find the nearest safe house
                safe_house = find_nearest_safe_house(grid, i, j)
                
                # Calculate the Manhattan distance between the spy and the safe house
                distance = abs(i - safe_house[0]) + abs(j - safe_house[1])
                
                # Update the maximum distance if necessary
                if distance > max_distance:
                    max_distance = distance
    
    # Return the maximum distance
    return max_distance

def find_nearest_safe_house(grid, i, j):
    # Initialize the nearest safe house as the current block
    nearest_safe_house = (i, j)
    
    # Loop through each block in the grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # If the current block is a safe house and it is closer to the spy than the current nearest safe house
            if grid[row][col] == "H" and abs(row - i) + abs(col - j) < abs(nearest_safe_house[0] - i) + abs(nearest_safe_house[1] - j):
                # Update the nearest safe house
                nearest_safe_house = (row, col)
    
    # Return the nearest safe house
    return nearest_safe_house

grid = [
    [".", ".", ".", "H"],
    [".", "S", ".", "."],
    [".", ".", ".", "H"],
    [".", ".", ".", "."]
]

print(get_max_distance(grid))

