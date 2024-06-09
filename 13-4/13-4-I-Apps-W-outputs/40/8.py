
import math

def solve(n, s, locations):
    # Calculate the total population of all locations
    total_population = sum(location[2] for location in locations)

    # Check if the city can become a megacity
    if total_population < s:
        return "-1"

    # Calculate the minimum radius of the circle that the city needs to expand to in order to become a megacity
    min_radius = math.sqrt(s / math.pi)

    # Check if the city can be expanded to the minimum radius
    if min_radius <= locations[0][0]:
        return str(min_radius)

    # Calculate the maximum distance from the city center to any location on the circle
    max_distance = max(math.sqrt(location[0]**2 + location[1]**2) for location in locations)

    # Check if the city can be expanded to the maximum distance
    if max_distance <= min_radius:
        return str(max_distance)

    # The city cannot become a megacity
    return "-1"

