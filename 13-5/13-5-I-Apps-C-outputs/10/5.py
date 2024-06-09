
def get_cheapest_network(n, m, p, insecure_buildings, connections):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for x, y, cost in connections:
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))

    # Find the minimum cost of connecting all insecure buildings
    min_cost = float("inf")
    for i in range(n):
        if i + 1 in insecure_buildings:
            for j in range(n):
                if j + 1 in insecure_buildings:
                    continue
                cost = get_path_cost(graph, i, j)
                if cost < min_cost:
                    min_cost = cost

    # Return the minimum cost of connecting all buildings if possible, otherwise return "impossible"
    return min_cost if min_cost != float("inf") else "impossible"

def get_path_cost(graph, start, end):
    # Initialize a set to keep track of visited nodes
    visited = set()

    # Initialize a queue to do BFS
    queue = [(start, 0)]

    # Do BFS until the end node is reached
    while queue:
        node, cost = queue.pop(0)
        if node == end:
            return cost
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node]:
            queue.append((neighbor, cost + weight))

    # If the end node is not reached, return infinity
    return float("inf")

n, m, p = map(int, input().split())
insecure_buildings = set(map(int, input().split()))
connections = []
for _ in range(m):
    x, y, cost = map(int, input().split())
    connections.append((x, y, cost))
print(get_cheapest_network(n, m, p, insecure_buildings, connections))

