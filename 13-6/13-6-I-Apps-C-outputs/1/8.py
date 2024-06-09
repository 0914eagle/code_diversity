
def f1(n, m, p, insecure_buildings, connections):
    # create a graph with n nodes (buildings) and m edges (direct connections)
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
    for connection in connections:
        x, y, cost = connection
        graph[x].append((y, cost))
        graph[y].append((x, cost))
    
    # find the shortest path between each pair of buildings using Dijkstra's algorithm
    from heapq import heappop, heappush
    dist = {i: float('inf') for i in range(1, n + 1)}
    prev = {i: None for i in range(1, n + 1)}
    q = [(0, 1)]
    while q:
        cost, node = heappop(q)
        if dist[node] < cost:
            continue
        for neighbor, cost in graph[node]:
            new_cost = cost + dist[node]
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                prev[neighbor] = node
                heappush(q, (new_cost, neighbor))
    
    # check if the security measure is satisfied
    for i in range(1, n + 1):
        if i in insecure_buildings:
            continue
        for j in range(1, n + 1):
            if j in insecure_buildings:
                continue
            if dist[i] + dist[j] != dist[j] + dist[i]:
                return -1
    
    # return the cost of the cheapest network
    return dist[n]

def f2(n, m, p, insecure_buildings, connections):
    # create a graph with n nodes (buildings) and m edges (direct connections)
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
    for connection in connections:
        x, y, cost = connection
        graph[x].append((y, cost))
        graph[y].append((x, cost))
    
    # find the minimum spanning tree of the graph
    from heapq import heappop, heappush
    dist = {i: float('inf') for i in range(1, n + 1)}
    prev = {i: None for i in range(1, n + 1)}
    q = [(0, 1)]
    while q:
        cost, node = heappop(q)
        if dist[node] < cost:
            continue
        for neighbor, cost in graph[node]:
            new_cost = cost + dist[node]
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                prev[neighbor] = node
                heappush(q, (new_cost, neighbor))
    
    # check if the security measure is satisfied
    for i in range(1, n + 1):
        if i in insecure_buildings:
            continue
        for j in range(1, n + 1):
            if j in insecure_buildings:
                continue
            if dist[i] + dist[j] != dist[j] + dist[i]:
                return -1
    
    # return the cost of the cheapest network
    return dist[n]

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    connections = []
    for _ in range(m):
        x, y, cost = map(int, input().split())
        connections.append((x, y, cost))
    
    print(f1(n, m, p, insecure_buildings, connections))
    print(f2(n, m, p, insecure_buildings, connections))

