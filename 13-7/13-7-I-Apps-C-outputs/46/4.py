
def get_cheapest_network(n, m, p, insecure_buildings, direct_connections):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the direct connections
    for x, y, cost in direct_connections:
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))

    # Find the minimum spanning tree of the graph
    parent = [-1] * n
    key = [float('inf')] * n
    key[0] = 0
    mst = []
    for _ in range(n - 1):
        min_cost = float('inf')
        min_index = -1
        for i in range(n):
            if key[i] < min_cost and parent[i] == -1:
                min_cost = key[i]
                min_index = i
        u = min_index
        for i in range(len(graph[u])):
            v, w = graph[u][i]
            if key[v] > key[u] + w:
                key[v] = key[u] + w
                parent[v] = u
        mst.append((u + 1, v + 1, w))

    # Check if the network is secure
    for u, v, w in mst:
        if u in insecure_buildings and v in insecure_buildings:
            return -1

    # Return the cost of the network
    return sum(w for _, _, w in mst)

def main():
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    direct_connections = []
    for _ in range(m):
        x, y, cost = map(int, input().split())
        direct_connections.append((x, y, cost))
    print(get_cheapest_network(n, m, p, insecure_buildings, direct_connections))

if __name__ == '__main__':
    main()

