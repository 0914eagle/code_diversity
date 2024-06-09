
import math

def solve(n, s, locations):
    # Calculate the total population of all locations
    total_population = sum(location[2] for location in locations)

    # Check if the total population is greater than the required population for a megacity
    if total_population < s:
        return -1

    # Calculate the minimum radius needed to include all locations in a circle
    min_radius = 0
    for location in locations:
        min_radius = max(min_radius, math.sqrt(location[0]**2 + location[1]**2))

    return min_radius

