
def get_maximum_reachable_vertices_plan(n, m, s, edges):
    # Initialize the plan with all undirected edges
    plan = ['-'] * m
    
    # Create a graph with all undirected edges
    graph = {}
    for i in range(n):
        graph[i + 1] = []
    for edge in edges:
        if edge[0] == 2:
            graph[edge[1]].append(edge[2])
            graph[edge[2]].append(edge[1])
    
    # DFS to find the reachable vertices from the starting vertex
    visited = [False] * (n + 1)
    queue = [s]
    visited[s] = True
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    
    # Find the maximum number of reachable vertices
    max_reachable_vertices = 0
    for i in range(n):
        if visited[i + 1]:
            max_reachable_vertices += 1
    
    # Orient the undirected edges to maximize the number of reachable vertices
    for i in range(m):
        if edges[i][0] == 2:
            if not visited[edges[i][1]] or not visited[edges[i][2]]:
                plan[i] = '+'
    
    return max_reachable_vertices, plan

def get_minimum_reachable_vertices_plan(n, m, s, edges):
    # Initialize the plan with all undirected edges
    plan = ['-'] * m
    
    # Create a graph with all undirected edges
    graph = {}
    for i in range(n):
        graph[i + 1] = []
    for edge in edges:
        if edge[0] == 2:
            graph[edge[1]].append(edge[2])
            graph[edge[2]].append(edge[1])
    
    # DFS to find the reachable vertices from the starting vertex
    visited = [False] * (n + 1)
    queue = [s]
    visited[s] = True
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    
    # Find the minimum number of reachable vertices
    min_reachable_vertices = 0
    for i in range(n):
        if visited[i + 1]:
            min_reachable_vertices += 1
    
    # Orient the undirected edges to minimize the number of reachable vertices
    for i in range(m):
        if edges[i][0] == 2:
            if not visited[edges[i][1]] and not visited[edges[i][2]]:
                plan[i] = '+'
    
    return min_reachable_vertices, plan

def main():
    n, m, s = map(int, input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    
    max_reachable_vertices, plan = get_maximum_reachable_vertices_plan(n, m, s, edges)
    min_reachable_vertices, plan = get_minimum_reachable_vertices_plan(n, m, s, edges)
    
    print(max_reachable_vertices)
    print("".join(plan))
    print(min_reachable_vertices)
    print("".join(plan))

if __name__ == '__main__':
    main()

