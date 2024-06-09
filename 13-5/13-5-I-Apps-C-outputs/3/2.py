
def get_max_flow(n, m, s, t, edges):
    # Initialize the graph with the given nodes and edges
    graph = {i: set() for i in range(n)}
    for u, v, c in edges:
        graph[u].add((v, c))
        graph[v].add((u, c))
    
    # Initialize the residual graph with the given edges
    residual = {i: set() for i in range(n)}
    for u, v, c in edges:
        residual[u].add((v, c))
        residual[v].add((u, 0))
    
    # Initialize the flow value for each edge to 0
    flow = {(u, v): 0 for u, v, c in edges}
    
    # Initialize the parent and depth arrays
    parent = [-1] * n
    depth = [0] * n
    
    # Function to find the augmenting path
    def bfs(s, t):
        queue = [(s, 0)]
        while queue:
            u, d = queue.pop(0)
            if u == t:
                return d
            for v, c in graph[u]:
                if c > 0 and depth[v] == 0:
                    depth[v] = d + 1
                    parent[v] = u
                    queue.append((v, d + 1))
        return 0
    
    # Function to calculate the minimum residual capacity of an edge
    def get_min_residual_capacity(u, v):
        for v, c in residual[u]:
            if v == parent[u]:
                return c
        return 0
    
    # Function to update the flow and residual graphs
    def update_graphs(u, v, f):
        for i in range(n):
            for j in range(n):
                if i == u and j == v:
                    residual[i].remove((j, flow[(i, j)]))
                    residual[j].remove((i, flow[(i, j)]))
                    flow[(i, j)] = 0
                elif i == u and j != v:
                    residual[i].remove((j, flow[(i, j)]))
                    residual[j].add((i, flow[(i, j)]))
                    flow[(i, j)] = 0
                elif i != u and j == v:
                    residual[i].add((j, flow[(i, j)]))
                    residual[j].remove((i, flow[(i, j)]))
                    flow[(i, j)] = 0
                else:
                    residual[i].add((j, flow[(i, j)]))
                    residual[j].add((i, flow[(i, j)]))
                    flow[(i, j)] = 0
    
    # Function to find the maximum flow
    def find_max_flow(s, t):
        while bfs(s, t):
            path = []
            v = t
            while v != s:
                u = parent[v]
                path.append((u, v, get_min_residual_capacity(u, v)))
                v = u
            path.reverse()
            f = min([c for u, v, c in path])
            for u, v, c in path:
                update_graphs(u, v, f)
            return f
    
    # Find the maximum flow
    f = find_max_flow(s, t)
    
    # Print the results
    print(n, f, m)
    for u, v, c in edges:
        if flow[(u, v)] > 0:
            print(u, v, flow[(u, v)])

