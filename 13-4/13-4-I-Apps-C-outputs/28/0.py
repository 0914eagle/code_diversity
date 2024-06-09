
def f1(n, m, p, insecure_buildings, connections):
    # create a graph with n nodes (buildings) and m edges (direct connections)
    graph = [[] for _ in range(n)]
    for x, y, cost in connections:
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
            dfs(neighbor)
            mst.append((node, neighbor, cost))
    
    dfs(0)
    
    # check if the MST satisfies the security measure
    for node in range(n):
        if node in insecure_buildings:
            for neighbor, cost in graph[node]:
                if neighbor in insecure_buildings and (node, neighbor) not in mst:
                    return -1
    
    # return the total cost of the MST
    return sum(cost for _, _, cost in mst)

def f2(n, m, p, insecure_buildings, connections):
    # create a graph with n nodes (buildings) and m edges (direct connections)
    graph = [[] for _ in range(n)]
    for x, y, cost in connections:
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
            dfs(neighbor)
            mst.append((node, neighbor, cost))
    
    dfs(0)
    
    # check if the MST satisfies the security measure
    for node in range(n):
        if node in insecure_buildings:
            for neighbor, cost in graph[node]:
                if neighbor in insecure_buildings and (node, neighbor) not in mst:
                    return -1
    
    # return the total cost of the MST
    return sum(cost for _, _, cost in mst)

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    connections = []
    for _ in range(m):
        x, y, cost = map(int, input().split())
        connections.append((x, y, cost))
    print(f1(n, m, p, insecure_buildings, connections))

