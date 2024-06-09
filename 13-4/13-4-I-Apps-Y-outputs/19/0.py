
def get_max_distance(grid):
    # Initialize variables
    max_distance = 0
    spy_location = None
    safe_houses = []

    # Loop through the grid to find the spy and safe houses
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                safe_houses.append((i, j))
            elif grid[i][j] == "S":
                spy_location = (i, j)

    # Loop through the safe houses and calculate the Manhattan distance from the spy to each safe house
    for safe_house in safe_houses:
        distance = abs(safe_house[0] - spy_location[0]) + abs(safe_house[1] - spy_location[1])
        if distance > max_distance:
            max_distance = distance

    return max_distance

