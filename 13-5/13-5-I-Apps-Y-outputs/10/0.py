
def get_input():
    n = int(input())
    edges = []
    for i in range(n - 1):
        edges.append(tuple(map(int, input().split())))
    return n, edges

def find_maximum_edges(n, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}
    for edge in edges:
        neighbors[edge[0]].add(edge[1])
        neighbors[edge[1]].add(edge[0])
    
    # Initialize a set to store the selected vertices
    selected = set()
    
    # Initialize a dictionary to store the maximum number of edges for each vertex
    max_edges = {i: 0 for i in range(1, n + 1)}
    
    # Iterate through the vertices and find the maximum number of edges for each vertex
    for vertex in range(1, n + 1):
        if vertex not in selected:
            selected.add(vertex)
            queue = [vertex]
            while queue:
                current = queue.pop(0)
                for neighbor in neighbors[current]:
                    if neighbor not in selected:
                        queue.append(neighbor)
                        selected.add(neighbor)
                        max_edges[neighbor] = max(max_edges[neighbor], max_edges[current] + 1)
    
    # Find the vertex with the maximum number of edges
    max_vertex = max(max_edges, key=max_edges.get)
    
    # Find the two vertices that are not adjacent to the maximum vertex
    non_adjacent_vertices = [vertex for vertex in range(1, n + 1) if vertex not in neighbors[max_vertex]]
    
    # Find the third vertex that is not adjacent to the maximum vertex
    third_vertex = non_adjacent_vertices[0]
    
    return max_edges[max_vertex], max_vertex, third_vertex

def get_output(n, edges, max_edges, max_vertex, third_vertex):
    print(max_edges)
    print(max_vertex, third_vertex)

if __name__ == '__main__':
    n, edges = get_input()
    max_edges, max_vertex, third_vertex = find_maximum_edges(n, edges)
    get_output(n, edges, max_edges, max_vertex, third_vertex)

