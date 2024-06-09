
def solve(N, M, roads):
    # Initialize a dictionary to store the number of roads connected to each city
    num_roads = {i: 0 for i in range(1, N + 1)}
    
    # Iterate over the roads and increment the number of roads connected to each city
    for road in roads:
        city1, city2 = road
        num_roads[city1] += 1
        num_roads[city2] += 1
    
    # Return the number of roads connected to each city
    return [num_roads[i] for i in range(1, N + 1)]

