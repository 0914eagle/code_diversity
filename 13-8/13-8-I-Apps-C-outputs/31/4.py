
def get_min_distance(planet_positions):
    # Initialize the minimum distance to travel as 0
    min_distance = 0

    # Loop through each planet position
    for i in range(len(planet_positions)):
        # Get the current planet position
        current_planet = planet_positions[i]

        # Loop through each other planet position
        for j in range(i + 1, len(planet_positions)):
            # Get the other planet position
            other_planet = planet_positions[j]

            # Calculate the distance between the current planet and the other planet
            distance = get_distance(current_planet, other_planet)

            # If the distance is less than the minimum distance, update the minimum distance
            if distance < min_distance:
                min_distance = distance

    # Return the minimum distance
    return min_distance

def get_distance(planet1, planet2):
    # Calculate the Euclidean distance between the two planets
    distance = ((planet1[0] - planet2[0]) ** 2 + (planet1[1] - planet2[1]) ** 2 + (planet1[2] - planet2[2]) ** 2) ** 0.5

    # Return the distance
    return distance

planet_positions = [[0, 0, 1], [0, 1, 1], [2, 0, 3], [2, 1, 3]]
print(get_min_distance(planet_positions))

