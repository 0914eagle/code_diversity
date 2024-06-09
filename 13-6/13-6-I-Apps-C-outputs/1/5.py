
def f1(n, m, p, insecure_buildings, costs):
    # create a graph with n nodes (buildings) and m edges (direct connections)
    graph = {}
    for i in range(n):
        graph[i] = []
    for i in range(m):
        x, y, cost = costs[i]
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))
    
    # find the minimum spanning tree of the graph
    parent = [-1] * n
    key = [float('inf')] * n
    key[0] = 0
    queue = [(0, 0)]
    while queue:
        node, dist = queue.pop(0)
        for neighbor, cost in graph[node]:
            if key[neighbor] > dist + cost:
                key[neighbor] = dist + cost
                parent[neighbor] = node
        for neighbor, _ in graph[node]:
            if neighbor not in insecure_buildings and neighbor != parent[node]:
                queue.append((neighbor, dist + cost))
    
    # calculate the total cost of the network
    total_cost = 0
    for i in range(n):
        if i in insecure_buildings:
            total_cost += key[i]
    
    return total_cost

def f2(n, m, p, insecure_buildings, costs):
    # create a graph with n nodes (buildings) and m edges (direct connections)
    graph = {}
    for i in range(n):
        graph[i] = []
    for i in range(m):
        x, y, cost = costs[i]
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))
    
    # find the minimum spanning tree of the graph
    parent = [-1] * n
    key = [float('inf')] * n
    key[0] = 0
    queue = [(0, 0)]
    while queue:
        node, dist = queue.pop(0)
        for neighbor, cost in graph[node]:
            if key[neighbor] > dist + cost:
                key[neighbor] = dist + cost
                parent[neighbor] = node
        for neighbor, _ in graph[node]:
            if neighbor not in insecure_buildings and neighbor != parent[node]:
                queue.append((neighbor, dist + cost))
    
    # calculate the total cost of the network
    total_cost = 0
    for i in range(n):
        if i in insecure_buildings:
            total_cost += key[i]
    
    return total_cost

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    costs = [tuple(map(int, input().split())) for _ in range(m)]
    print(f1(n, m, p, insecure_buildings, costs))
    print(f2(n, m, p, insecure_buildings, costs))

