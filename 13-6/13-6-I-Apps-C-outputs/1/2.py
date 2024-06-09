
def get_cheapest_network(n, m, p, insecure_buildings, costs):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for x, y, cost in costs:
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))

    # Find the shortest path between all pairs of nodes
    distances = [float('inf')] * n
    distances[0] = 0
    queue = [(0, 0)]
    while queue:
        node, distance = queue.pop(0)
        for neighbor, cost in graph[node]:
            if distance + cost < distances[neighbor]:
                distances[neighbor] = distance + cost
                queue.append((neighbor, distances[neighbor]))

    # Check if it is possible to connect all buildings securely
    secure_cost = 0
    for i in range(n):
        if i not in insecure_buildings:
            secure_cost += distances[i]
    if secure_cost == float('inf'):
        return "impossible"

    # Return the cheapest network cost
    return secure_cost

def main():
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    costs = []
    for _ in range(m):
        x, y, cost = map(int, input().split())
        costs.append((x, y, cost))
    print(get_cheapest_network(n, m, p, insecure_buildings, costs))

if __name__ == '__main__':
    main()

