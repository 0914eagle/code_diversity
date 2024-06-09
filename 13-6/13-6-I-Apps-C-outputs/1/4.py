
def f1(n, m, p, insecure_buildings, costs):
    # create a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for x, y, cost in costs:
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))
    
    # find the minimum spanning tree of the graph
    mst = []
    visited = set()
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
                mst.append((node, neighbor, cost))
    
    dfs(0)
    
    # calculate the total cost of the mst
    total_cost = 0
    for node1, node2, cost in mst:
        total_cost += cost
    
    # check if the mst satisfies the security measure
    for building in insecure_buildings:
        if building in visited:
            return "impossible"
    
    return total_cost

def f2(n, m, p, insecure_buildings, costs):
    # create a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for x, y, cost in costs:
        graph[x - 1].append((y - 1, cost))
        graph[y - 1].append((x - 1, cost))
    
    # find the minimum spanning tree of the graph
    mst = []
    visited = set()
    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        for neighbor, cost in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
                mst.append((node, neighbor, cost))
    
    dfs(0)
    
    # calculate the total cost of the mst
    total_cost = 0
    for node1, node2, cost in mst:
        total_cost += cost
    
    # check if the mst satisfies the security measure
    for building in insecure_buildings:
        if building in visited:
            return "impossible"
    
    return total_cost

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    costs = []
    for _ in range(m):
        x, y, cost = map(int, input().split())
        costs.append((x, y, cost))
    
    print(f1(n, m, p, insecure_buildings, costs))
    print(f2(n, m, p, insecure_buildings, costs))

