
def get_max_reachable_vertices(n, m, s, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1])
        graph[edge[1] - 1].append(edge[0])
    
    # Initialize a dictionary to store the reachable vertices from vertex s
    reachable_vertices = {s: 1}
    
    # Breadth-first search to find the maximum reachable vertices from vertex s
    queue = [s]
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex - 1]:
            if neighbor not in reachable_vertices:
                reachable_vertices[neighbor] = 1
                queue.append(neighbor)
    
    return len(reachable_vertices)

def get_min_reachable_vertices(n, m, s, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1])
        graph[edge[1] - 1].append(edge[0])
    
    # Initialize a dictionary to store the reachable vertices from vertex s
    reachable_vertices = {s: 1}
    
    # Breadth-first search to find the minimum reachable vertices from vertex s
    queue = [s]
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex - 1]:
            if neighbor not in reachable_vertices:
                reachable_vertices[neighbor] = 1
                queue.append(neighbor)
    
    return len(reachable_vertices)

def get_oriented_edges(n, m, s, edges):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for edge in edges:
        graph[edge[0] - 1].append(edge[1])
        graph[edge[1] - 1].append(edge[0])
    
    # Initialize a dictionary to store the reachable vertices from vertex s
    reachable_vertices = {s: 1}
    
    # Breadth-first search to find the reachable vertices from vertex s
    queue = [s]
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex - 1]:
            if neighbor not in reachable_vertices:
                reachable_vertices[neighbor] = 1
                queue.append(neighbor)
    
    # Initialize a list to store the oriented edges
    oriented_edges = []
    
    # Add the oriented edges to the list
    for edge in edges:
        if edge[0] in reachable_vertices and edge[1] in reachable_vertices:
            oriented_edges.append(edge)
    
    return oriented_edges

def main():
    n, m, s = map(int, input().split())
    edges = []
    for _ in range(m):
        t, u, v = map(int, input().split())
        edges.append([t, u, v])
    
    max_reachable_vertices = get_max_reachable_vertices(n, m, s, edges)
    min_reachable_vertices = get_min_reachable_vertices(n, m, s, edges)
    oriented_edges = get_oriented_edges(n, m, s, edges)
    
    print(max_reachable_vertices)
    print("".join(["+" if edge[0] == s else "-" for edge in oriented_edges]))
    print(min_reachable_vertices)
    print("".join(["+" if edge[0] == s else "-" for edge in oriented_edges]))

if __name__ == "__main__":
    main()

