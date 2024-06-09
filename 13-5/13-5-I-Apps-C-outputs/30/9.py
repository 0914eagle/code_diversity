
def f1(n, m, roads, k, orders):
    # f1 should return the longest time a customer has to wait from the time they place their order until the order is delivered
    
    # Initialize a graph with n nodes and m edges
    graph = {}
    for i in range(n):
        graph[i] = []
    for road in roads:
        graph[road[0]].append((road[1], road[2]))
        graph[road[1]].append((road[0], road[2]))
    
    # Initialize a priority queue to store the orders
    pq = []
    for order in orders:
        heapq.heappush(pq, (order[0], order[1]))
    
    # Initialize a dictionary to store the distances from the pizzeria to each intersection
    distances = {1: 0}
    for i in range(2, n+1):
        distances[i] = float('inf')
    
    # Dijkstra's algorithm to find the shortest distances from the pizzeria to each intersection
    while pq:
        time, intersection = heapq.heappop(pq)
        if intersection not in distances:
            continue
        for neighbor, weight in graph[intersection]:
            distance = distances[intersection] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (time+distance, neighbor))
    
    # Find the longest time a customer has to wait from the time they place their order until the order is delivered
    max_wait_time = 0
    for order in orders:
        wait_time = distances[order[1]] - order[0]
        if wait_time > max_wait_time:
            max_wait_time = wait_time
    
    return max_wait_time

def f2(...):
    # f2 should return the optimal delivery schedule
    pass

if __name__ == '__main__':
    n, m, roads, k, orders = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(m)]
    orders = [list(map(int, input().split())) for _ in range(k)]
    print(f1(n, m, roads, k, orders))

