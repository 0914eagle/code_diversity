
def get_connected_roads(n, m, roads):
    connected_roads = [0] * (n + 1)
    for road in roads:
        connected_roads[road[0]] += 1
        connected_roads[road[1]] += 1
    return connected_roads[1:]

