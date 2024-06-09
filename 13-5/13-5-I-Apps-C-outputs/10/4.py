
def get_cheapest_network(n, m, p, insecure_buildings, connections):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for connection in connections:
        x, y, cost = connection
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))

    # Find the minimum cost flow from source (0) to sink (n - 1) in the graph
    flow = float("inf")
    for i in range(n):
        if i + 1 not in insecure_buildings:
            continue
        for j in range(n):
            if j + 1 in insecure_buildings:
                continue
            flow = min(flow, find_min_cost_flow(graph, i, j))

    return flow if flow < float("inf") else "impossible"

def find_min_cost_flow(graph, source, sink):
    # Initialize a queue and a visited array
    queue = [source]
    visited = [False] * len(graph)

    # Loop until the queue is empty
    while queue:
        # Dequeue a node from the queue
        node = queue.pop(0)

        # If the node is the sink, return the minimum cost flow
        if node == sink:
            return 0

        # If the node has not been visited, mark it as visited and add its neighbors to the queue
        if not visited[node]:
            visited[node] = True
            for neighbor, cost in graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)

    # If the sink is not reachable from the source, return infinity
    return float("inf")

