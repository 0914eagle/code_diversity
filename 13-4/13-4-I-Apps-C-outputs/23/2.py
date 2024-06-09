
def f1(N, P, X):
    # Initialize the graph with N vertices and P as the parent of each vertex
    graph = [[] for _ in range(N)]
    for i in range(1, N):
        graph[P[i]].append(i)
    
    # Initialize the color and weight of each vertex as None
    color = [None] * (N + 1)
    weight = [None] * (N + 1)
    
    # Set the color and weight of the root vertex (Vertex 1)
    color[1] = "white"
    weight[1] = X[1]
    
    # Recursively assign colors and weights to the vertices in the subtree
    def assign_colors(u, parent):
        nonlocal color, weight
        for v in graph[u]:
            if v != parent:
                color[v] = "black" if color[u] == "white" else "white"
                weight[v] = X[v]
                assign_colors(v, u)
    
    assign_colors(1, None)
    
    # Check if the condition is satisfied for all vertices
    for u in range(1, N + 1):
        if weight[u] != X[u]:
            return "IMPOSSIBLE"
    
    return "POSSIBLE"

def f2(N, P, X):
    # Initialize the graph with N vertices and P as the parent of each vertex
    graph = [[] for _ in range(N)]
    for i in range(1, N):
        graph[P[i]].append(i)
    
    # Initialize the color and weight of each vertex as None
    color = [None] * (N + 1)
    weight = [None] * (N + 1)
    
    # Set the color and weight of the root vertex (Vertex 1)
    color[1] = "white"
    weight[1] = X[1]
    
    # Recursively assign colors and weights to the vertices in the subtree
    def assign_colors(u, parent):
        nonlocal color, weight
        for v in graph[u]:
            if v != parent:
                color[v] = "black" if color[u] == "white" else "white"
                weight[v] = X[v]
                assign_colors(v, u)
    
    assign_colors(1, None)
    
    # Check if the condition is satisfied for all vertices
    for u in range(1, N + 1):
        if weight[u] != X[u]:
            return "IMPOSSIBLE"
    
    return "POSSIBLE"

if __name__ == '__main__':
    N, P, X = map(int, input().split())
    print(f1(N, P, X))
    print(f2(N, P, X))

