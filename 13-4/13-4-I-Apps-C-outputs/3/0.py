
def is_graph_valid(n, m, edges):
    # Initialize a dictionary to store the degrees of each vertex
    degrees = {}
    for i in range(1, n + 1):
        degrees[i] = 0
    
    # Iterate over the edges and update the degrees of the vertices
    for edge in edges:
        u, v = edge[0], edge[1]
        degrees[u] += 1
        degrees[v] += 1
    
    # Check if the degrees of all vertices are either 1 or 2
    for degree in degrees.values():
        if degree not in [1, 2]:
            return False
    
    # Check if the graph is connected
    visited = set()
    queue = [1]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue += [neighbor for neighbor in degrees if neighbor != vertex]
    
    return len(visited) == n

def solve(n, m, edges):
    # Check if the given graph is valid
    if not is_graph_valid(n, m, edges):
        return "No"
    
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {}
    for i in range(1, n + 1):
        neighbors[i] = set()
    
    # Iterate over the edges and update the neighbors of each vertex
    for edge in edges:
        u, v = edge[0], edge[1]
        neighbors[u].add(v)
        neighbors[v].add(u)
    
    # Initialize a list to store the possible strings
    strings = []
    
    # Recursively generate all possible strings
    def generate_strings(string, vertex):
        if len(string) == n:
            strings.append(string)
            return
        
        for neighbor in neighbors[vertex]:
            if neighbor not in string:
                generate_strings(string + chr(neighbor + 96), neighbor)
    
    generate_strings("", 1)
    
    # Check if any of the generated strings correspond to the given graph
    for string in strings:
        graph = [set() for _ in range(n + 1)]
        for i in range(1, n):
            u, v = string[i - 1], string[i]
            if u != v and (u == chr(v.upper() + 32) or v == chr(u.upper() + 32)):
                graph[i].add(i + 1)
        
        if graph == edges:
            return "Yes\n" + string
    
    return "No"

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    print(solve(n, m, edges))

