
def is_graph_valid(n, m, edges):
    # Initialize a dictionary to store the degrees of each vertex
    degrees = {}
    for i in range(1, n + 1):
        degrees[i] = 0
    
    # Iterate over the edges and update the degrees of the vertices
    for edge in edges:
        u, v = edge
        degrees[u] += 1
        degrees[v] += 1
    
    # Check if the degrees of all vertices are even
    for degree in degrees.values():
        if degree % 2 == 1:
            return False
    
    # Check if the graph is connected
    visited = set()
    queue = [1]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(edges[vertex])
    
    return len(visited) == n

def find_string(n, edges):
    # Initialize a list to store the possible strings
    strings = []
    
    # Iterate over the edges and update the possible strings
    for edge in edges:
        u, v = edge
        for string in strings:
            if string[u - 1] == string[v - 1] or (string[u - 1] == "a" and string[v - 1] == "b") or (string[u - 1] == "b" and string[v - 1] == "c"):
                strings.append(string)
    
    # Return any of the possible strings
    return strings[0] if strings else ""

def main():
    n, m = map(int, input().split())
    edges = [tuple(map(int, input().split())) for _ in range(m)]
    if is_graph_valid(n, m, edges):
        print("Yes")
        print(find_string(n, edges))
    else:
        print("No")

if __name__ == '__main__':
    main()

