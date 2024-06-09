
def is_graph_reconstructable(n, m, edges):
    
    # Initialize a dictionary to keep track of the edges in the graph
    edge_dict = {}
    for edge in edges:
        u, v = edge
        if u not in edge_dict:
            edge_dict[u] = []
        edge_dict[u].append(v)
    
    # Initialize a set to keep track of the vertices that have been visited
    visited = set()
    
    # Recursively explore the graph starting from vertex 1
    if explore_graph(1, edge_dict, visited, n):
        return True
    else:
        return False

def explore_graph(vertex, edge_dict, visited, n):
    
    # If all vertices have been visited, return True
    if len(visited) == n:
        return True
    
    # If the current vertex has not been visited, mark it as visited and explore its neighbors
    if vertex not in visited:
        visited.add(vertex)
        for neighbor in edge_dict[vertex]:
            if explore_graph(neighbor, edge_dict, visited, n):
                return True
    
    # If the current vertex has been visited and all of its neighbors have been visited, return False
    return False

def reconstruct_string(n, m, edges):
    
    # Initialize an empty string
    string = ""
    
    # Initialize a dictionary to keep track of the vertices that have been visited
    visited = {}
    
    # Recursively explore the graph starting from vertex 1
    explore_graph(1, edges, visited, n)
    
    # Fill in the string with the letters corresponding to the visited vertices
    for vertex in range(1, n + 1):
        if vertex in visited:
            string += "a"
        else:
            string += "b"
    
    return string

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    if is_graph_reconstructable(n, m, edges):
        print("Yes")
        print(reconstruct_string(n, m, edges))
    else:
        print("No")

if __name__ == '__main__':
    main()

