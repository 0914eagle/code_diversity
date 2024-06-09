
def is_graph_solvable(n, m, edges):
    # Initialize a dictionary to store the degrees of each vertex
    degrees = {}
    for i in range(1, n + 1):
        degrees[i] = 0
    
    # Iterate over the edges and increment the degree of each vertex
    for edge in edges:
        u, v = edge[0], edge[1]
        degrees[u] += 1
        degrees[v] += 1
    
    # Check if the degrees of all vertices are equal
    for degree in degrees.values():
        if degree != m:
            return "No"
    
    # Initialize a list to store the possible strings
    strings = []
    
    # Iterate over the edges and generate all possible strings
    for edge in edges:
        u, v = edge[0], edge[1]
        if u == v - 1:
            strings.append("a" + strings[-1][1:])
        elif u == v + 1:
            strings.append(strings[-1][:-1] + "c")
        else:
            strings.append("a" + strings[-1][1:] + "c")
    
    # Check if any of the generated strings form the original graph
    for string in strings:
        if n == len(string) == m:
            graph = {}
            for i in range(n):
                graph[i + 1] = [j + 1 for j in range(i + 1, n) if string[j] in ("b", "c")]
            if graph == edges:
                return "Yes\n" + string
    
    return "No"

