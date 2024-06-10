
def get_cost(n, m, p, insecure_buildings, connections):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for connection in connections:
        x, y, cost = connection
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))

    # Find the shortest path between all pairs of nodes
    distances = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        distances[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    # Check if the security measure is satisfied
    for i in range(n):
        for j in range(n):
            if i != j and distances[i][j] != float('inf'):
                for insecure_building in insecure_buildings:
                    if insecure_building == i or insecure_building == j:
                        continue
                    if distances[i][j] > distances[i][insecure_building] + distances[insecure_building][j]:
                        return -1

    # Return the cost of the cheapest network
    return sum(cost for connection in connections)

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

