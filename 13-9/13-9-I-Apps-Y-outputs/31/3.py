
def get_road_counts(cities, roads):
    # Initialize a dictionary to store the number of roads connected to each city
    road_counts = {city: 0 for city in cities}

    # Iterate over the roads and increment the number of roads connected to each city
    for road in roads:
        city1, city2 = road
        road_counts[city1] += 1
        road_counts[city2] += 1

    return [road_counts[city] for city in cities]

