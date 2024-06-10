
def get_diameter(n, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
    
    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Find the longest shortest path in the graph
    diameter = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if graph[i] and graph[j] and not set(graph[i]).isdisjoint(graph[j]):
                diameter = max(diameter, len(graph[i]) + len(graph[j]))
    
    return diameter

def add_edges(n, edges):
    # Initialize a dictionary to store the graph
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []
    
    # Add edges to the graph
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    
    # Find the longest shortest path in the graph
    diameter = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if graph[i] and graph[j] and not set(graph[i]).isdisjoint(graph[j]):
                diameter = max(diameter, len(graph[i]) + len(graph[j]))
    
    # Add edges to form a tree with minimum diameter
    added_edges = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if graph[i] and graph[j] and not set(graph[i]).isdisjoint(graph[j]) and len(graph[i]) + len(graph[j]) == diameter:
                added_edges.append((i, j))
    
    return added_edges

def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    
    diameter = get_diameter(n, edges)
    added_edges = add_edges(n, edges)
    
    print(diameter)
    for edge in added_edges:
        print(*edge)

if __name__ == '__main__':
    main()

