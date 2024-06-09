
def get_min_extra_roads(n, m, s, roads):
    # Initialize a set to store the reachable cities from the capital
    reachable_cities = set([s])
    # Loop through each road
    for road in roads:
        # If the road is from the capital to a new city, add it to the set of reachable cities
        if road[0] == s:
            reachable_cities.add(road[1])
    # Return the number of extra roads needed to make all cities reachable from the capital
    return n - len(reachable_cities)

