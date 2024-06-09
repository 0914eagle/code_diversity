
def min_distance_travel(planets):
    # Initialize the minimum distance to travel as 0
    min_dist = 0
    # Loop through each planet in the list
    for i in range(len(planets)):
        # Calculate the distance between the current planet and the next planet
        dist = calc_distance(planets[i], planets[(i+1)%len(planets)])
        # Add the distance to the minimum distance
        min_dist += dist
    return min_dist

def calc_distance(planet1, planet2):
    # Calculate the Euclidean distance between the two planets
    return ((planet1[0]-planet2[0])**2 + (planet1[1]-planet2[1])**2 + (planet1[2]-planet2[2])**2)**0.5

