
def get_min_distance(planet_positions):
    # Initialize the minimum distance to travel
    min_distance = 0

    # Loop through each planet position
    for i in range(len(planet_positions)):
        # Get the current planet position
        current_position = planet_positions[i]

        # Loop through each other planet position
        for j in range(i + 1, len(planet_positions)):
            # Get the other planet position
            other_position = planet_positions[j]

            # Calculate the distance between the current and other planets
            distance = get_distance(current_position, other_position)

            # If the distance is less than the minimum distance, update the minimum distance
            if distance < min_distance:
                min_distance = distance

    # Return the minimum distance
    return min_distance

def get_distance(position1, position2):
    # Calculate the distance between the two positions
    distance = ((position1[0] - position2[0]) ** 2 + (position1[1] - position2[1]) ** 2 + (position1[2] - position2[2]) ** 2) ** 0.5

    # Return the distance
    return distance

planet_positions = [(0, 0, 1), (0, 1, 1), (2, 0, 3), (2, 1, 3)]
print(get_min_distance(planet_positions))

