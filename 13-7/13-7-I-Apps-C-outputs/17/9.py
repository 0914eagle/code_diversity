
def solve(n, m, roads, orders):
    # Initialize a graph with n nodes (road intersections) and m edges (roads)
    graph = [[] for _ in range(n)]
    for u, v, d in roads:
        graph[u-1].append((v-1, d))
        graph[v-1].append((u-1, d))
    
    # Initialize a priority queue to store the delivery times for each order
    pq = [(0, 0)]
    visited = set()
    
    # Loop through the orders and add them to the priority queue
    for s, u, t in orders:
        pq.append((s, u-1))
        visited.add(u-1)
    
    # Loop through the priority queue and find the longest time it takes to deliver an order
    max_time = 0
    while pq:
        time, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (time+weight, neighbor))
        max_time = max(max_time, time)
    
    return max_time

