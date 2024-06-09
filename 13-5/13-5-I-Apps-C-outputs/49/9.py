
def get_minimum_path_length(n, m, roads):
    # Initialize a dictionary to store the length of the path from each station to the endpoint
    station_to_endpoint_length = {}
    for road in roads:
        u, v = road
        if u not in station_to_endpoint_length:
            station_to_endpoint_length[u] = 1
        if v not in station_to_endpoint_length:
            station_to_endpoint_length[v] = 1
        station_to_endpoint_length[u] = max(station_to_endpoint_length[u], station_to_endpoint_length[v] + 1)
    
    # Initialize a dictionary to store the length of the path from each station to the starting station
    station_to_starting_length = {}
    for road in roads:
        u, v = road
        if v not in station_to_starting_length:
            station_to_starting_length[v] = 1
        if u not in station_to_starting_length:
            station_to_starting_length[u] = 1
        station_to_starting_length[v] = max(station_to_starting_length[v], station_to_starting_length[u] + 1)
    
    # Find the maximum length path
    max_length = max(station_to_endpoint_length.values())
    
    # Find the minimum length path that a racer can achieve if at most one of the roads is blocked off
    min_length = float('inf')
    for road in roads:
        u, v = road
        if station_to_endpoint_length[u] + station_to_starting_length[v] - 1 < min_length:
            min_length = station_to_endpoint_length[u] + station_to_starting_length[v] - 1
    
    return min_length

def main():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        u, v = map(int, input().split())
        roads.append((u, v))
    print(get_minimum_path_length(n, m, roads))

if __name__ == '__main__':
    main()

