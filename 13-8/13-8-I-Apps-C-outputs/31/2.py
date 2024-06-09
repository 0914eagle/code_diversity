
def get_minimum_distance(planets):
    # Initialize the minimum distance to travel
    min_distance = 0

    # Loop through each planet in the list
    for i in range(len(planets)):
        # Get the current planet's position
        current_planet = planets[i]

        # Loop through each other planet in the list
        for j in range(i+1, len(planets)):
            # Get the other planet's position
            other_planet = planets[j]

            # Calculate the distance between the current planet and the other planet
            distance = get_distance(current_planet, other_planet)

            # If the distance is less than the minimum distance, update the minimum distance
            if distance < min_distance:
                min_distance = distance

    # Return the minimum distance
    return min_distance

def get_distance(planet1, planet2):
    # Calculate the distance between the two planets
    distance = ((planet1[0] - planet2[0]) ** 2 + (planet1[1] - planet2[1]) ** 2 + (planet1[2] - planet2[2]) ** 2) ** 0.5

    # Return the distance
    return distance

planets = [[0, 0, 1], [0, 1, 1], [2, 0, 3], [2, 1, 3]]
print(get_minimum_distance(planets))

