
def f1(n, m, p, insecure_buildings, costs):
    # create a graph with n nodes (buildings) and m edges (direct connections)
    graph = [[] for _ in range(n)]
    for i in range(m):
        x, y, cost = costs[i]
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))
    
    # find the minimum spanning tree of the graph
    parent = [0] * n
    key = [float('inf')] * n
    key[0] = 0
    mst = []
    for i in range(n - 1):
        for j in range(n):
            if key[j] < float('inf') and parent[j] == 0:
                for neighbor, cost in graph[j]:
                    if key[neighbor] > key[j] + cost:
                        key[neighbor] = key[j] + cost
                        parent[neighbor] = j
        mst.append((parent[n - 1], key[n - 1]))
    
    # check if the network satisfies the security measure
    for i in range(n):
        if i in insecure_buildings:
            for j in range(n):
                if j in insecure_buildings and j != i:
                    if any(neighbor == j for neighbor, _ in graph[i]):
                        return "impossible"
    
    # return the cost of the network
    return sum(cost for _, cost in mst)

def f2(n, m, p, insecure_buildings, costs):
    # create a graph with n nodes (buildings) and m edges (direct connections)
    graph = [[] for _ in range(n)]
    for i in range(m):
        x, y, cost = costs[i]
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))
    
    # find the minimum spanning tree of the graph
    parent = [0] * n
    key = [float('inf')] * n
    key[0] = 0
    mst = []
    for i in range(n - 1):
        for j in range(n):
            if key[j] < float('inf') and parent[j] == 0:
                for neighbor, cost in graph[j]:
                    if key[neighbor] > key[j] + cost:
                        key[neighbor] = key[j] + cost
                        parent[neighbor] = j
        mst.append((parent[n - 1], key[n - 1]))
    
    # check if the network satisfies the security measure
    for i in range(n):
        if i in insecure_buildings:
            for j in range(n):
                if j in insecure_buildings and j != i:
                    if any(neighbor == j for neighbor, _ in graph[i]):
                        return "impossible"
    
    # return the cost of the network
    return sum(cost for _, cost in mst)

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    costs = [tuple(map(int, input().split())) for _ in range(m)]
    print(f1(n, m, p, insecure_buildings, costs))

