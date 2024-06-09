
def f1(n, m, roads, k, orders):
    # create a graph representing the roads in Stockholm
    graph = {}
    for u, v, d in roads:
        if u not in graph:
            graph[u] = {}
        graph[u][v] = d
    
    # create a priority queue to store the orders
    pq = []
    for s, u, t in orders:
        heapq.heappush(pq, (s, u, t))
    
    # dijkstra's algorithm to find the shortest path from the pizzeria to each customer
    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    visited = set()
    while pq:
        s, u, t = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
    
    # find the maximum delay for each order
    max_delay = 0
    for s, u, t in orders:
        delay = dist[u] + t - s
        if delay > max_delay:
            max_delay = delay
    
    return max_delay

def f2(n, m, roads, k, orders):
    # create a graph representing the roads in Stockholm
    graph = {}
    for u, v, d in roads:
        if u not in graph:
            graph[u] = {}
        graph[u][v] = d
    
    # create a priority queue to store the orders
    pq = []
    for s, u, t in orders:
        heapq.heappush(pq, (s, u, t))
    
    # dijkstra's algorithm to find the shortest path from the pizzeria to each customer
    dist = [float('inf')] * (n + 1)
    dist[1] = 0
    visited = set()
    while pq:
        s, u, t = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)
        for v in graph[u]:
            if dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]
    
    # find the maximum delay for each order
    max_delay = 0
    for s, u, t in orders:
        delay = dist[u] + t - s
        if delay > max_delay:
            max_delay = delay
    
    return max_delay

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
    print(f1(n, m, roads, k, orders))
    print(f2(n, m, roads, k, orders))

