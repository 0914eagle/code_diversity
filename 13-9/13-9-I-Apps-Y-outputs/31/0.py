
def solve(N, M, roads):
    # Initialize a dictionary to store the number of roads connected to each city
    city_roads = {}
    for i in range(1, N+1):
        city_roads[i] = 0
    
    # Iterate through the roads and increment the number of roads connected to each city
    for road in roads:
        city1, city2 = road[0], road[1]
        city_roads[city1] += 1
        city_roads[city2] += 1
    
    # Return the number of roads connected to each city
    return [city_roads[i] for i in range(1, N+1)]

