
def f1(n, m, k, x_edges, y_edges, a_routes, b_routes):
    # Initialize graph with edge weights
    graph = {}
    for i in range(m):
        graph[x_edges[i]] = {y_edges[i]: w_edges[i]}
    
    # Initialize distance matrix with infinity
    distance = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        distance[i][i] = 0
    
    # Floyd-Warshall algorithm to find shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    # Calculate total cost for each route
    total_cost = 0
    for i in range(k):
        total_cost += distance[a_routes[i]][b_routes[i]]
    
    return total_cost

def f2(n, m, k, x_edges, y_edges, a_routes, b_routes):
    # Initialize graph with edge weights
    graph = {}
    for i in range(m):
        graph[x_edges[i]] = {y_edges[i]: w_edges[i]}
    
    # Initialize distance matrix with infinity
    distance = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        distance[i][i] = 0
    
    # Floyd-Warshall algorithm to find shortest paths
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    
    # Find the minimum cost edge
    min_cost = float('inf')
    min_edge = None
    for i in range(m):
        if distance[x_edges[i]][y_edges[i]] < min_cost:
            min_cost = distance[x_edges[i]][y_edges[i]]
            min_edge = (x_edges[i], y_edges[i])
    
    # Update graph with zero cost edge
    graph[min_edge[0]][min_edge[1]] = 0
    graph[min_edge[1]][min_edge[0]] = 0
    
    # Calculate total cost for each route
    total_cost = 0
    for i in range(k):
        total_cost += distance[a_routes[i]][b_routes[i]]
    
    return total_cost

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    x_edges = []
    y_edges = []
    w_edges = []
    for i in range(m):
        x, y, w = map(int, input().split())
        x_edges.append(x)
        y_edges.append(y)
        w_edges.append(w)
    a_routes = []
    b_routes = []
    for i in range(k):
        a, b = map(int, input().split())
        a_routes.append(a)
        b_routes.append(b)
    
    print(f1(n, m, k, x_edges, y_edges, a_routes, b_routes))
    print(f2(n, m, k, x_edges, y_edges, a_routes, b_routes))

