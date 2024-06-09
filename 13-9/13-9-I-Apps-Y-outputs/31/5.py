
def solve(n, m, roads):
    # Initialize a dictionary to store the number of roads connected to each city
    roads_connected = {i: 0 for i in range(1, n + 1)}

    # Iterate over the roads and increment the number of roads connected to each city
    for road in roads:
        city1, city2 = road
        roads_connected[city1] += 1
        roads_connected[city2] += 1

    # Return the number of roads connected to each city
    return [roads_connected[i] for i in range(1, n + 1)]

