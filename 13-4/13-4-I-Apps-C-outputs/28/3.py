
def f1(n, m, p, insecure_buildings, direct_lines):
    # Initialize the graph with the direct lines
    graph = {i: set() for i in range(1, n + 1)}
    for x, y, cost in direct_lines:
        graph[x].add((y, cost))
        graph[y].add((x, cost))

    # Add the insecure buildings to the graph
    for building in insecure_buildings:
        graph[building] = set()

    # Find the cheapest path from each building to each other building
    paths = {}
    for building in range(1, n + 1):
        paths[building] = dijkstra(graph, building)

    # Check if the security measure is satisfied for each path
    for building in range(1, n + 1):
        for other_building in range(building + 1, n + 1):
            path = paths[building][other_building]
            if path is None:
                continue
            for building in insecure_buildings:
                if building in path:
                    return "impossible"

    # Return the cheapest path
    return min(paths[building][other_building] for building in range(1, n + 1) for other_building in range(building + 1, n + 1))

def dijkstra(graph, start):
    visited = set()
    queue = [(0, start)]
    while queue:
        cost, building = heapq.heappop(queue)
        if building in visited:
            continue
        visited.add(building)
        for neighbor, neighbor_cost in graph[building]:
            heapq.heappush(queue, (cost + neighbor_cost, neighbor))
    return {building: cost for building, cost in queue}

def f2(n, m, p, insecure_buildings, direct_lines):
    # Initialize the graph with the direct lines
    graph = {i: set() for i in range(1, n + 1)}
    for x, y, cost in direct_lines:
        graph[x].add((y, cost))
        graph[y].add((x, cost))

    # Add the insecure buildings to the graph
    for building in insecure_buildings:
        graph[building] = set()

    # Find the cheapest path from each building to each other building
    paths = {}
    for building in range(1, n + 1):
        paths[building] = dijkstra(graph, building)

    # Check if the security measure is satisfied for each path
    for building in range(1, n + 1):
        for other_building in range(building + 1, n + 1):
            path = paths[building][other_building]
            if path is None:
                continue
            for building in insecure_buildings:
                if building in path:
                    return "impossible"

    # Return the cheapest path
    return min(paths[building][other_building] for building in range(1, n + 1) for other_building in range(building + 1, n + 1))

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    direct_lines = []
    for _ in range(m):
        x, y, cost = map(int, input().split())
        direct_lines.append((x, y, cost))
    print(f1(n, m, p, insecure_buildings, direct_lines))

