
def get_max_distance(grid):
    # Initialize variables
    max_distance = 0
    spy_location = None
    safe_houses = []

    # Find the location of the spy and the safe houses
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                spy_location = (i, j)
            elif grid[i][j] == "H":
                safe_houses.append((i, j))

    # Calculate the distance from the spy to each safe house
    for safe_house in safe_houses:
        distance = abs(safe_house[0] - spy_location[0]) + abs(safe_house[1] - spy_location[1])
        if distance > max_distance:
            max_distance = distance

    return max_distance

