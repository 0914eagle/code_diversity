
def f1(n, m, roads, orders):
    # create a graph with n nodes (road intersections) and m edges (roads)
    graph = {i: set() for i in range(1, n + 1)}
    for u, v, d in roads:
        graph[u].add((v, d))
        graph[v].add((u, d))

    # find the shortest path from the pizzeria to each customer using Dijkstra's algorithm
    dist = {1: 0}
    prev = {1: None}
    q = [(0, 1)]
    while q:
        _, u = heappop(q)
        if u not in dist:
            continue
        for v, d in graph[u]:
            alt = dist[u] + d
            if v not in dist or alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heappush(q, (alt, v))

    # calculate the longest waiting time for each customer
    max_wait = 0
    for s, u, t in orders:
        path = []
        v = u
        while v != 1:
            path.append(v)
            v = prev[v]
        path.reverse()
        wait = 0
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            wait += dist[u] - dist[v]
        max_wait = max(max_wait, wait + t - s)

    return max_wait

def f2(n, m, roads, orders):
    # create a graph with n nodes (road intersections) and m edges (roads)
    graph = {i: set() for i in range(1, n + 1)}
    for u, v, d in roads:
        graph[u].add((v, d))
        graph[v].add((u, d))

    # find the shortest path from the pizzeria to each customer using Dijkstra's algorithm
    dist = {1: 0}
    prev = {1: None}
    q = [(0, 1)]
    while q:
        _, u = heappop(q)
        if u not in dist:
            continue
        for v, d in graph[u]:
            alt = dist[u] + d
            if v not in dist or alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heappush(q, (alt, v))

    # calculate the longest waiting time for each customer
    max_wait = 0
    for s, u, t in orders:
        path = []
        v = u
        while v != 1:
            path.append(v)
            v = prev[v]
        path.reverse()
        wait = 0
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            wait += dist[u] - dist[v]
        max_wait = max(max_wait, wait + t - s)

    return max_wait

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

