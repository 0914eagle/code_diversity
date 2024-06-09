
def find_max_distance(grid):
    # Initialize variables
    max_distance = 0
    safe_houses = []

    # Find all safe houses in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "H":
                safe_houses.append((i, j))

    # Find the nearest safe house for each spy
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "S":
                # Find the distance to the nearest safe house
                min_distance = float("inf")
                for safe_house in safe_houses:
                    distance = abs(i - safe_house[0]) + abs(j - safe_house[1])
                    if distance < min_distance:
                        min_distance = distance

                # Update the maximum distance
                if min_distance > max_distance:
                    max_distance = min_distance

    return max_distance

