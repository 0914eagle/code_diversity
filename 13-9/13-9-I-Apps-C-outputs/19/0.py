
def find_min_path_length(n, m, roads):
    # Initialize a dictionary to store the length of the path from each station to the endpoint
    station_to_endpoint_length = {}
    for road in roads:
        u, v = road[0], road[1]
        if u not in station_to_endpoint_length:
            station_to_endpoint_length[u] = 1
        if v not in station_to_endpoint_length:
            station_to_endpoint_length[v] = 1
        station_to_endpoint_length[u] = max(station_to_endpoint_length[u], station_to_endpoint_length[v] + 1)
    
    # Initialize a dictionary to store the length of the path from each station to the starting station
    station_to_starting_length = {}
    for road in roads:
        u, v = road[0], road[1]
        if v not in station_to_starting_length:
            station_to_starting_length[v] = 1
        if u not in station_to_starting_length:
            station_to_starting_length[u] = 1
        station_to_starting_length[v] = max(station_to_starting_length[v], station_to_starting_length[u] + 1)
    
    # Find the maximum length path
    max_length = max(station_to_endpoint_length.values())
    
    # Find the minimum length path that a racer can take if at most one road is blocked off
    min_length = max_length
    for road in roads:
        u, v = road[0], road[1]
        length_u_to_v = station_to_starting_length[u] + station_to_endpoint_length[v] - 2
        min_length = min(min_length, length_u_to_v)
    
    return min_length

