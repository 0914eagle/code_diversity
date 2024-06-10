
def get_cost(m, n, p, insecure_buildings, connections):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph
    for connection in connections:
        x, y, cost = connection
        graph[x].append((y, cost))
        graph[y].append((x, cost))

    # Find the shortest path between all pairs of vertices using Dijkstra's algorithm
    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    q = [(0, 1)]
    while q:
        cost, vertex = heapq.heappop(q)
        if dist[vertex] < cost:
            continue
        for neighbor, weight in graph[vertex]:
            new_cost = cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(q, (new_cost, neighbor))

    # Check if the cost of the path from the first building to the last building is less than or equal to the total cost of the network
    total_cost = sum(cost for _, cost in connections)
    if dist[-1] <= total_cost:
        return dist[-1]
    else:
        return -1

def main():
    m, n, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    connections = []
    for _ in range(m):
        x, y, cost = map(int, input().split())
        connections.append((x, y, cost))
    print(get_cost(m, n, p, insecure_buildings, connections))

if __name__ == '__main__':
    main()

