
def get_tree_edges(n, edges):
    # Create a dictionary to store the edges of the tree
    tree_edges = {}
    for edge in edges:
        tree_edges[edge[0]] = tree_edges.get(edge[0], []) + [edge[1]]
        tree_edges[edge[1]] = tree_edges.get(edge[1], []) + [edge[0]]
    
    # Return the tree edges
    return tree_edges

def get_paths(tree_edges, a, b, c):
    # Initialize the paths between a and b, b and c, and a and c
    paths_ab = []
    paths_bc = []
    paths_ac = []
    
    # Create a queue to store the vertices to visit
    queue = [a]
    
    # Loop until the queue is empty
    while queue:
        # Get the current vertex from the queue
        current_vertex = queue.pop(0)
        
        # If the current vertex is b, add it to the paths between a and b and b and c
        if current_vertex == b:
            paths_ab.append(current_vertex)
            paths_bc.append(current_vertex)
        
        # If the current vertex is c, add it to the paths between a and c and b and c
        if current_vertex == c:
            paths_ac.append(current_vertex)
            paths_bc.append(current_vertex)
        
        # Add the neighbors of the current vertex to the queue
        for neighbor in tree_edges[current_vertex]:
            if neighbor not in queue:
                queue.append(neighbor)
    
    # Return the paths between a and b, b and c, and a and c
    return paths_ab, paths_bc, paths_ac

def get_maximum_edges(tree_edges, a, b, c):
    # Get the paths between a and b, b and c, and a and c
    paths_ab, paths_bc, paths_ac = get_paths(tree_edges, a, b, c)
    
    # Initialize the maximum number of edges
    max_edges = 0
    
    # Loop through the paths and count the number of edges
    for path in paths_ab + paths_bc + paths_ac:
        max_edges += len(path)
    
    # Return the maximum number of edges
    return max_edges

def get_vertices(tree_edges, max_edges):
    # Initialize the vertices with the maximum number of edges
    vertices = []
    
    # Loop through the tree edges
    for vertex in tree_edges:
        # Get the number of edges for the current vertex
        num_edges = len(tree_edges[vertex])
        
        # If the number of edges is equal to the maximum number of edges, add the vertex to the list of vertices
        if num_edges == max_edges:
            vertices.append(vertex)
    
    # Return the list of vertices
    return vertices

def main():
    # Read the number of vertices and edges
    n, m = map(int, input().split())
    
    # Read the edges
    edges = []
    for _ in range(m):
        edges.append(list(map(int, input().split())))
    
    # Get the tree edges
    tree_edges = get_tree_edges(n, edges)
    
    # Get the maximum number of edges
    max_edges = get_maximum_edges(tree_edges, 1, 5, 6)
    
    # Get the vertices with the maximum number of edges
    vertices = get_vertices(tree_edges, max_edges)
    
    # Print the result
    print(max_edges)
    print(" ".join(map(str, vertices)))

if __name__ == '__main__':
    main()

