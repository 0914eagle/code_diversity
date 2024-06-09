
def f1(n, m, p, insecure_buildings, costs):
    # create a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for i in range(m):
        x, y, cost = costs[i]
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))
    
    # find the shortest path between all pairs of nodes
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # check if the network is secure
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] != float('inf') and i not in insecure_buildings and j not in insecure_buildings:
                return -1
    
    # find the cheapest path between all pairs of nodes
    cost = 0
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] != float('inf'):
                cost += dist[i][j]
    
    return cost

def f2(n, m, p, insecure_buildings, costs):
    # create a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for i in range(m):
        x, y, cost = costs[i]
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))
    
    # find the shortest path between all pairs of nodes
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    # check if the network is secure
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] != float('inf') and i not in insecure_buildings and j not in insecure_buildings:
                return -1
    
    # find the cheapest path between all pairs of nodes
    cost = 0
    for i in range(n):
        for j in range(n):
            if i != j and dist[i][j] != float('inf'):
                cost += dist[i][j]
    
    return cost

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    costs = []
    for i in range(m):
        x, y, cost = map(int, input().split())
        costs.append((x, y, cost))
    
    cost = f1(n, m, p, insecure_buildings, costs)
    if cost == -1:
        print("Impossible")
    else:
        print(cost)

