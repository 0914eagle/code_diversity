
def f1(n, m, p, insecure_buildings, cost_matrix):
    # Initialize the graph with the given cost matrix
    graph = cost_matrix
    
    # Add the insecure buildings to the graph
    for building in insecure_buildings:
        graph[building][building] = 0
    
    # Find the minimum spanning tree of the graph
    mst = kruskal(graph)
    
    # Calculate the total cost of the MST
    total_cost = 0
    for edge in mst:
        total_cost += graph[edge[0]][edge[1]]
    
    return total_cost

def f2(n, m, p, insecure_buildings, cost_matrix):
    # Initialize the graph with the given cost matrix
    graph = cost_matrix
    
    # Add the insecure buildings to the graph
    for building in insecure_buildings:
        graph[building][building] = 0
    
    # Find the minimum spanning tree of the graph
    mst = prim(graph)
    
    # Calculate the total cost of the MST
    total_cost = 0
    for edge in mst:
        total_cost += graph[edge[0]][edge[1]]
    
    return total_cost

def kruskal(graph):
    # Find the minimum spanning tree of the graph using Kruskal's algorithm
    mst = []
    for edge in sorted(graph.items(), key=lambda x: x[1]):
        if not is_cycle(mst + [edge]):
            mst.append(edge)
    
    return mst

def prim(graph):
    # Find the minimum spanning tree of the graph using Prim's algorithm
    mst = []
    visited = set()
    while len(mst) < len(graph) - 1:
        min_cost = float('inf')
        min_edge = None
        for edge in graph.items():
            if edge[0] not in visited and edge[1] not in visited and edge[1] < min_cost:
                min_cost = edge[1]
                min_edge = edge
        mst.append(min_edge)
        visited.add(min_edge[0])
        visited.add(min_edge[1])
    
    return mst

def is_cycle(edges):
    # Check if the given edges form a cycle
    visited = set()
    for edge in edges:
        if edge[0] in visited or edge[1] in visited:
            return True
        visited.add(edge[0])
        visited.add(edge[1])
    
    return False

if __name__ == '__main__':
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    cost_matrix = {}
    for i in range(m):
        x, y, cost = map(int, input().split())
        if x not in cost_matrix:
            cost_matrix[x] = {}
        if y not in cost_matrix:
            cost_matrix[y] = {}
        cost_matrix[x][y] = cost
        cost_matrix[y][x] = cost
    
    print(f1(n, m, p, insecure_buildings, cost_matrix))
    print(f2(n, m, p, insecure_buildings, cost_matrix))

