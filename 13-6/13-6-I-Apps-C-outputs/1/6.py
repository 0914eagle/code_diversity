
def f1(n, m, p, insecure_buildings, connections):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for connection in connections:
        graph[connection[0] - 1].append((connection[1], connection[2]))
        graph[connection[1] - 1].append((connection[0], connection[2]))

    # Find the shortest path between all pairs of nodes
    distances = [float('inf')] * n
    distances[0] = 0
    queue = [(0, 0)]
    while queue:
        node, distance = queue.pop(0)
        for neighbor, weight in graph[node]:
            if distance + weight < distances[neighbor]:
                distances[neighbor] = distance + weight
                queue.append((neighbor, distances[neighbor]))

    # Check if it is possible to reach all insecure buildings from the first building
    for i in range(1, n):
        if i not in insecure_buildings and distances[i] == float('inf'):
            return -1

    # Find the cheapest path to all insecure buildings
    total_cost = 0
    for i in range(1, n):
        if i in insecure_buildings:
            total_cost += distances[i]

    return total_cost

def f2(n, m, p, insecure_buildings, connections):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for connection in connections:
        graph[connection[0] - 1].append((connection[1], connection[2]))
        graph[connection[1] - 1].append((connection[0], connection[2]))

    # Find the shortest path between all pairs of nodes
    distances = [float('inf')] * n
    distances[0] = 0
    queue = [(0, 0)]
    while queue:
        node, distance = queue.pop(0)
        for neighbor, weight in graph[node]:
            if distance + weight < distances[neighbor]:
                distances[neighbor] = distance + weight
                queue.append((neighbor, distances[neighbor]))

    # Check if it is possible to reach all insecure buildings from the first building
    for i in range(1, n):
        if i not in insecure_buildings and distances[i] == float('inf'):
            return -1

    # Find the cheapest path to all insecure buildings
    total_cost = 0
    for i in range(1, n):
        if i in insecure_buildings:
            total_cost += distances[i]

    return total_cost

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    connections = []
    for i in range(m):
        x, y, cost = map(int, input().split())
        connections.append((x, y, cost))
    print(f1(n, m, p, insecure_buildings, connections))

