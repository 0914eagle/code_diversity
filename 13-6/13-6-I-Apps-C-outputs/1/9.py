
def get_cost(n, m, p, insecure_buildings, connections):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for connection in connections:
        x, y, cost = connection
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))

    # Find the minimum spanning tree of the graph
    mst = prim(graph, 0)

    # Calculate the total cost of the MST
    total_cost = sum(cost for _, cost in mst)

    # Check if the MST satisfies the security measure
    for i in range(n):
        for j in range(i + 1, n):
            if i in insecure_buildings and j in insecure_buildings and (i, j) in mst:
                return "impossible"

    return total_cost

def prim(graph, start):
    # Initialize the priority queue with the start vertex and its distance from the start vertex
    pq = [(0, start)]

    # Initialize the distances and parents arrays
    distances = [float("inf") for _ in graph]
    parents = [-1 for _ in graph]

    # Set the start vertex distance to 0
    distances[start] = 0

    # Loop until the priority queue is empty
    while pq:
        # Get the vertex with the minimum distance from the priority queue
        u = heappop(pq)[1]

        # Loop through the neighbors of the current vertex
        for v, cost in graph[u]:
            # If the distance to the neighbor is greater than the current distance, update the distance and the parent
            if distances[v] > distances[u] + cost:
                distances[v] = distances[u] + cost
                parents[v] = u

        # Add the neighbor to the priority queue if it has not been visited yet
        if distances[v] < float("inf"):
            heappush(pq, (distances[v], v))

    # Return the minimum spanning tree
    return [(u + 1, v + 1, cost) for u, v, cost in zip(parents, range(len(graph)), distances) if u != -1]

def main():
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    connections = [tuple(map(int, input().split())) for _ in range(m)]
    print(get_cost(n, m, p, insecure_buildings, connections))

if __name__ == '__main__':
    main()

