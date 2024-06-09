
def get_cheapest_network(n, m, p, insecure_buildings, direct_connections):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the direct connections
    for x, y, cost in direct_connections:
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))

    # Find the minimum spanning tree of the graph
    mst = kruskal(graph)

    # Calculate the total cost of the MST
    total_cost = sum(cost for _, cost in mst)

    # Check if the MST satisfies the security measure
    for i in range(n):
        for j in range(i + 1, n):
            if i in insecure_buildings or j in insecure_buildings:
                continue
            if any(k in insecure_buildings for k in get_path(mst, i, j)):
                return "impossible"

    return total_cost

def get_path(mst, i, j):
    path = []
    while i != j:
        for node, cost in mst:
            if node == i:
                path.append(i)
                i = node
                break
        else:
            break
    return path

def kruskal(graph):
    mst = []
    for node in range(len(graph)):
        mst.append((node, float('inf')))
    for edge in graph:
        mst.sort(key=lambda x: x[1])
        mst.pop(0)
    return mst

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    direct_connections = [tuple(map(int, input().split())) for _ in range(m)]
    print(get_cheapest_network(n, m, p, insecure_buildings, direct_connections))

