
def f1(n, m, p, insecure_buildings, costs):
    # create a graph with n nodes (buildings) and m edges (direct connections)
    graph = [[] for _ in range(n)]
    for x, y, cost in costs:
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))
    
    # find the shortest path between all pairs of buildings using Dijkstra's algorithm
    distances = [float('inf')] * n
    distances[0] = 0
    queue = [(0, 0)]
    while queue:
        building, distance = heapq.heappop(queue)
        if distance > distances[building]:
            continue
        for neighbor, cost in graph[building]:
            if distance + cost < distances[neighbor]:
                distances[neighbor] = distance + cost
                heapq.heappush(queue, (neighbor, distances[neighbor]))
    
    # check if the security measure is satisfied
    for building in range(n):
        if building in insecure_buildings:
            for neighbor in graph[building]:
                if distances[neighbor[0]] != float('inf'):
                    return -1
    
    # return the total cost of the network
    return sum(distances)

def f2(n, m, p, insecure_buildings, costs):
    # create a graph with n nodes (buildings) and m edges (direct connections)
    graph = [[] for _ in range(n)]
    for x, y, cost in costs:
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))
    
    # find the minimum spanning tree of the graph
    parent = [None] * n
    rank = [0] * n
    mst = []
    for building in range(n):
        if parent[building] is None:
            heapq.heappush(mst, (0, building))
            parent[building] = building
            rank[building] = 1
            while mst:
                distance, building = heapq.heappop(mst)
                for neighbor, cost in graph[building]:
                    if parent[neighbor] is None:
                        heapq.heappush(mst, (distance + cost, neighbor))
                        parent[neighbor] = building
                        rank[neighbor] = rank[building] + 1
    
    # check if the security measure is satisfied
    for building in range(n):
        if building in insecure_buildings:
            for neighbor in graph[building]:
                if rank[neighbor] != 1:
                    return -1
    
    # return the total cost of the network
    return sum(cost for _, cost in costs)

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    costs = []
    for _ in range(m):
        x, y, cost = map(int, input().split())
        costs.append((x, y, cost))
    print(f1(n, m, p, insecure_buildings, costs))
    print(f2(n, m, p, insecure_buildings, costs))

