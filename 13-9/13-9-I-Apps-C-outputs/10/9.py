
def solve(fruit_garden):
    # Initialize variables
    row_count, col_count = len(fruit_garden), len(fruit_garden[0])
    fall_locations = []
    distances = []

    # Find the fall locations and distances
    for i in range(row_count):
        for j in range(col_count):
            if fruit_garden[i][j] == "x":
                fall_locations.append((i, j))
                distances.append(0)
    for i in range(1, len(fall_locations)):
        previous_location = fall_locations[i - 1]
        current_location = fall_locations[i]
        distance = abs(previous_location[0] - current_location[0]) ** 2 + abs(previous_location[1] - current_location[1]) ** 2
        distances.append(distance)

    return distances

