
def find_min_separated_cities(n, roads):
    # Initialize a dictionary to store the cities and their neighbors
    cities = {i: set() for i in range(1, n + 1)}

    # Add the neighbors for each city
    for road in roads:
        cities[road[0]].add(road[1])
        cities[road[1]].add(road[0])

    # Initialize a set to store the separated cities
    separated_cities = set()

    # Iterate through the cities and their neighbors
    for city, neighbors in cities.items():
        # If the city has no neighbors, it is a separated city
        if not neighbors:
            separated_cities.add(city)

    # Return the minimum number of separated cities
    return len(separated_cities)

