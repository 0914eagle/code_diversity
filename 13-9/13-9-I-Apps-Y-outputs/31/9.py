
def get_number_of_roads_connected_to_city(n_cities, m_roads, roads):
    # Initialize a dictionary to store the number of roads connected to each city
    num_roads_per_city = {i: 0 for i in range(1, n_cities + 1)}

    # Iterate over the roads and increment the number of roads connected to each city
    for road in roads:
        city1, city2 = road
        num_roads_per_city[city1] += 1
        num_roads_per_city[city2] += 1

    # Return the number of roads connected to each city
    return [num_roads_per_city[i] for i in range(1, n_cities + 1)]

