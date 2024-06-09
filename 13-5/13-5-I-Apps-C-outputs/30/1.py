
def f1(n, m, roads, orders):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for u, v, d in roads:
        graph[u-1].append((v-1, d))
        graph[v-1].append((u-1, d))

    # Find the shortest path from node 0 (pizzeria) to all other nodes
    dist = [float('inf') for _ in range(n)]
    dist[0] = 0
    queue = [(0, 0)]
    while queue:
        node, cost = queue.pop(0)
        for neighbor, weight in graph[node]:
            if dist[neighbor] > dist[node] + weight:
                dist[neighbor] = dist[node] + weight
                queue.append((neighbor, dist[neighbor]))

    # Find the maximum delivery time
    max_delivery_time = 0
    for s, u, t in orders:
        delivery_time = dist[u-1] + t - s
        max_delivery_time = max(max_delivery_time, delivery_time)

    return max_delivery_time

def f2(n, m, roads, orders):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for u, v, d in roads:
        graph[u-1].append((v-1, d))
        graph[v-1].append((u-1, d))

    # Find the shortest path from node 0 (pizzeria) to all other nodes
    dist = [float('inf') for _ in range(n)]
    dist[0] = 0
    queue = [(0, 0)]
    while queue:
        node, cost = queue.pop(0)
        for neighbor, weight in graph[node]:
            if dist[neighbor] > dist[node] + weight:
                dist[neighbor] = dist[node] + weight
                queue.append((neighbor, dist[neighbor]))

    # Find the maximum delivery time
    max_delivery_time = 0
    for s, u, t in orders:
        delivery_time = dist[u-1] + t - s
        max_delivery_time = max(max_delivery_time, delivery_time)

    return max_delivery_time

if __name__ == '__main__':
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        u, v, d = map(int, input().split())
        roads.append((u, v, d))
    k = int(input())
    orders = []
    for _ in range(k):
        s, u, t = map(int, input().split())
        orders.append((s, u, t))
    print(f1(n, m, roads, orders))
    print(f2(n, m, roads, orders))

