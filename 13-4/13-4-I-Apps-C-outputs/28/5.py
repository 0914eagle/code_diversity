
def get_cost(n, m, p, insecure_buildings, connections):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for x, y, cost in connections:
        graph[x].append((y, cost))
        graph[y].append((x, cost))

    # Find the shortest path from each insecure building to each other building
    distances = [float('inf')] * (n + 1)
    for building in insecure_buildings:
        distances = dijkstra(graph, building, distances)

    # Calculate the total cost of the network
    total_cost = 0
    for x, y, cost in connections:
        total_cost += cost * (distances[x] + distances[y])

    return total_cost

def dijkstra(graph, start, distances):
    queue = [(0, start)]
    while queue:
        cost, building = heapq.heappop(queue)
        if cost < distances[building]:
            distances[building] = cost
            for neighbor, weight in graph[building]:
                heapq.heappush(queue, (cost + weight, neighbor))
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

