
def get_cost(n, m, p, insecure_buildings, connections):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for connection in connections:
        x, y, cost = connection
        graph[x].append((y, cost))
        graph[y].append((x, cost))

    # Find the shortest path from each insecure building to each other building
    shortest_paths = []
    for insecure_building in insecure_buildings:
        shortest_paths.append(dijkstra(graph, insecure_building))

    # Check if the cost of the cheapest network is less than or equal to the total cost of the shortest paths
    cheapest_network_cost = sum(shortest_paths[0])
    for i in range(1, len(shortest_paths)):
        if sum(shortest_paths[i]) > cheapest_network_cost:
            return "impossible"

    return cheapest_network_cost

def dijkstra(graph, source):
    # Initialize the priority queue with the source node
    queue = [(0, source)]

    # Initialize the distances and previous nodes
    distances = [float("inf") for _ in range(len(graph))]
    previous = [None for _ in range(len(graph))]
    distances[source] = 0

    while queue:
        # Get the node with the minimum distance from the queue
        dist, node = heappop(queue)

        # Check if the node has already been visited
        if distances[node] < dist:
            continue

        # Update the distances and previous nodes
        for neighbor, weight in graph[node]:
            distance = dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = node
                heappush(queue, (distance, neighbor))

    return distances

def main():
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    connections = []
    for _ in range(m):
        x, y, cost = map(int, input().split())
        connections.append((x, y, cost))
    print(get_cost(n, m, p, insecure_buildings, connections))

if __name__ == '__main__':
    main()

