
import sys
input = sys.stdin.read()

# Function to calculate Manhattan distance between two points
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Function to find the nearest safe house from a given position
def find_nearest_safe_house(grid, position):
    # Initialize the minimum distance and the nearest safe house
    min_distance = float('inf')
    nearest_safe_house = None
    
    # Iterate over the grid to find the nearest safe house
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'H':
                # Calculate the distance between the current position and the safe house
                distance = manhattan_distance((i, j), position)
                
                # If the distance is less than the minimum distance, update the minimum distance and the nearest safe house
                if distance < min_distance:
                    min_distance = distance
                    nearest_safe_house = (i, j)
    
    return nearest_safe_house

# Function to find the maximum Manhattan distance that any spy has to travel to reach the nearest safe house
def find_max_manhattan_distance(grid):
    # Initialize the maximum distance
    max_distance = 0
    
    # Iterate over the grid to find the maximum Manhattan distance
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # If the current position is a spy, find the nearest safe house and calculate the Manhattan distance
            if grid[i][j] == 'S':
                nearest_safe_house = find_nearest_safe_house(grid, (i, j))
                distance = manhattan_distance((i, j), nearest_safe_house)
                
                # If the distance is greater than the maximum distance, update the maximum distance
                if distance > max_distance:
                    max_distance = distance
    
    return max_distance

# Test the functions
grid = [
    ['.', '.', '.', '.', '.'],
    ['.', 'H', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', 'S', '.'],
]
print(find_max_manhattan_distance(grid)) # Output: 5

grid = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', 'S', '.'],
]
print(find_max_manhattan_distance(grid)) # Output: 4

grid = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
]
print(find_max_manhattan_distance(grid)) # Output: 0

