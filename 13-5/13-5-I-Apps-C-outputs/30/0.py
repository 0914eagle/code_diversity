
def f1(n, m, roads, orders):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for u, v, d in roads:
        graph[u-1].append((v-1, d))
        graph[v-1].append((u-1, d))

    # Find the shortest path from the pizzeria to each customer
    dist = [float('inf') for _ in range(n)]
    dist[0] = 0
    queue = [(0, 0)]
    while queue:
        u, cost = queue.pop(0)
        for v, d in graph[u]:
            if dist[v] > dist[u] + d:
                dist[v] = dist[u] + d
                queue.append((v, dist[v]))

    # Find the longest waiting time for each customer
    waiting_time = [0 for _ in range(n)]
    for s, u, t in orders:
        waiting_time[u-1] = max(waiting_time[u-1], t - s - dist[u-1])

    # Return the longest waiting time
    return max(waiting_time)

def f2(n, m, roads, orders):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for u, v, d in roads:
        graph[u-1].append((v-1, d))
        graph[v-1].append((u-1, d))

    # Find the shortest path from the pizzeria to each customer
    dist = [float('inf') for _ in range(n)]
    dist[0] = 0
    queue = [(0, 0)]
    while queue:
        u, cost = queue.pop(0)
        for v, d in graph[u]:
            if dist[v] > dist[u] + d:
                dist[v] = dist[u] + d
                queue.append((v, dist[v]))

    # Find the longest waiting time for each customer
    waiting_time = [0 for _ in range(n)]
    for s, u, t in orders:
        waiting_time[u-1] = max(waiting_time[u-1], t - s - dist[u-1])

    # Return the longest waiting time
    return max(waiting_time)

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

