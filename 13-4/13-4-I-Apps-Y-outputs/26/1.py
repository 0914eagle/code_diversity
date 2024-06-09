
def get_minimum_roads(n, m, s, roads):
    # Initialize a set to store the reachable cities from the capital
    reachable_cities = set([s])
    # Loop through each road
    for road in roads:
        # If the road connects two cities that are not already reachable from the capital
        if road[0] not in reachable_cities and road[1] not in reachable_cities:
            # Add both cities to the set of reachable cities
            reachable_cities.add(road[0])
            reachable_cities.add(road[1])
    # Return the number of cities that are not reachable from the capital
    return n - len(reachable_cities)

