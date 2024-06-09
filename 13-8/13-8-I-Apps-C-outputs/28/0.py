
def is_possible(n, m, edges):
    # Initialize a dictionary to store the degrees of each vertex
    degrees = {}
    for i in range(1, n + 1):
        degrees[i] = 0
    
    # Iterate over the edges and increment the degree of each vertex
    for edge in edges:
        u, v = edge[0], edge[1]
        degrees[u] += 1
        degrees[v] += 1
    
    # Check if the degrees of all vertices are either 1 or 2
    for degree in degrees.values():
        if degree not in [1, 2]:
            return False
    
    # Check if the graph is connected
    visited = set([1])
    queue = [1]
    while queue:
        vertex = queue.pop(0)
        for neighbor in edges:
            if neighbor[0] == vertex:
                if neighbor[1] not in visited:
                    visited.add(neighbor[1])
                    queue.append(neighbor[1])
    
    return len(visited) == n

def solve(n, m, edges):
    # Check if the graph is possible
    if is_possible(n, m, edges):
        # Initialize a list to store the vertices and their corresponding letters
        letters = ["a"] * n
        for edge in edges:
            u, v = edge[0], edge[1]
            if letters[u - 1] == "a":
                letters[u - 1] = "b"
            elif letters[u - 1] == "b":
                letters[u - 1] = "c"
            if letters[v - 1] == "a":
                letters[v - 1] = "b"
            elif letters[v - 1] == "b":
                letters[v - 1] = "c"
        return "".join(letters)
    else:
        return "No"

