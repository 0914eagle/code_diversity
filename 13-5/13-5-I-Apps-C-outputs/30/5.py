
def get_longest_wait_time(orders, roads, n):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n + 1)]

    # Add edges to the graph based on the roads
    for u, v, d in roads:
        graph[u].append((v, d))
        graph[v].append((u, d))

    # Dijkstra's algorithm to find the shortest path from the pizzeria to each customer
    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    q = [(0, 1)]
    while q:
        d, u = heappop(q)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[v] > d + w:
                dist[v] = d + w
                heappush(q, (dist[v], v))

    # Find the longest wait time by subtracting the delivery time from the order time
    longest_wait_time = 0
    for s, u, t in orders:
        wait_time = t - dist[u]
        if wait_time > longest_wait_time:
            longest_wait_time = wait_time

    return longest_wait_time

def main():
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
    print(get_longest_wait_time(orders, roads, n))

if __name__ == '__main__':
    main()

