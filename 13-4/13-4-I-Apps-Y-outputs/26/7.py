
def get_minimum_roads(n, m, s, roads):
    # Initialize a set to store the reachable cities from the capital
    reachable_cities = set([s])
    # Loop through each road
    for road in roads:
        # If the road is from the capital to a new city, add it to the reachable cities set
        if road[0] == s:
            reachable_cities.add(road[1])
    # Initialize a variable to store the number of extra roads needed
    extra_roads = 0
    # Loop through each city
    for city in range(1, n + 1):
        # If the city is not reachable from the capital, increment the number of extra roads needed
        if city not in reachable_cities:
            extra_roads += 1
    return extra_roads

