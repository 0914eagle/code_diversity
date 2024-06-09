
def get_min_time(n, m, railways):
    # Initialize a graph with the given railways
    graph = {i: set() for i in range(1, n + 1)}
    for u, v in railways:
        graph[u].add(v)
        graph[v].add(u)

    # Find all pairs of towns that are connected by a railway
    railway_pairs = set()
    for u in graph:
        for v in graph[u]:
            if u < v:
                railway_pairs.add((u, v))

    # Find all pairs of towns that are connected by a road
    road_pairs = set(railway_pairs)
    for u in graph:
        for v in graph[u]:
            if (u, v) in railway_pairs:
                road_pairs.remove((u, v))

    # Find the shortest path between the starting town and the destination town for the train and the bus
    train_path = bfs(graph, 1, n)
    bus_path = bfs(graph, 1, n, road_pairs)

    # If there is no path for either the train or the bus, return -1
    if not train_path or not bus_path:
        return -1

    # Find the maximum of the arrival times of the train and the bus
    max_time = 0
    for i in range(len(train_path) - 1):
        max_time = max(max_time, graph[train_path[i]][train_path[i + 1]])
    for i in range(len(bus_path) - 1):
        max_time = max(max_time, graph[bus_path[i]][bus_path[i + 1]])

    return max_time

def bfs(graph, start, end, avoid=None):
    queue = [(start, 0)]
    visited = set()
    while queue:
        town, time = queue.pop(0)
        if town == end:
            return [town]
        if town not in visited:
            visited.add(town)
            for neighbor in graph[town]:
                if neighbor not in visited and (avoid is None or (neighbor, town) not in avoid):
                    queue.append((neighbor, time + graph[town][neighbor]))
    return []

if __name__ == '__main__':
    n, m = map(int, input().split())
    railways = []
    for _ in range(m):
        u, v = map(int, input().split())
        railways.append((u, v))
    print(get_min_time(n, m, railways))

