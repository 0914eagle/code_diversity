
def solve(n, planets):
    # Initialize the minimum distance to travel
    min_distance = 0
    # Loop through each planet
    for i in range(n):
        # Find the distance to the current planet
        distance = find_distance(planets[i], planets[(i+1)%n])
        # Add the distance to the minimum distance
        min_distance += distance
    # Return the minimum distance
    return min_distance

def find_distance(planet1, planet2):
    # Find the Euclidean distance between the two planets
    distance = ((planet1[0]-planet2[0])**2 + (planet1[1]-planet2[1])**2 + (planet1[2]-planet2[2])**2)**0.5
    # Return the distance
    return distance

