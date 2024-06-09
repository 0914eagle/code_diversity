
def count_valid_pairs(n, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}

    # Add edges to the dictionary
    for edge in edges:
        neighbors[edge[0]].add(edge[1])
        neighbors[edge[1]].add(edge[0])

    # Initialize a set to store the valid pairs
    valid_pairs = set()

    # Iterate over all pairs of vertices
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # If the pair is valid, add it to the set of valid pairs
            if is_valid_pair(neighbors, i, j):
                valid_pairs.add((i, j))

    return len(valid_pairs)

def is_valid_pair(neighbors, i, j):
    # Initialize a stack to store the vertices to visit
    stack = [i]

    # Initialize a set to store the visited vertices
    visited = set()

    # Initialize a flag to indicate if a 1-edge has been encountered
    one_edge_encountered = False

    while stack:
        # Pop a vertex from the stack
        vertex = stack.pop()

        # If the vertex is the destination vertex, return True
        if vertex == j:
            return True

        # If the vertex has not been visited, mark it as visited and add its neighbors to the stack
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(neighbors[vertex])

        # If a 1-edge has been encountered and a 0-edge is encountered, return False
        if one_edge_encountered and vertex in neighbors[i] and neighbors[vertex][neighbors[vertex].index(vertex) - 1] == i:
            return False

        # If a 1-edge is encountered, set the flag to True
        if vertex in neighbors[i] and neighbors[vertex][neighbors[vertex].index(vertex) - 1] == i:
            one_edge_encountered = True

    # If the destination vertex is not found, return False
    return False

n = int(input())
edges = []
for i in range(n - 1):
    x, y, c = map(int, input().split())
    edges.append((x, y, c))
print(count_valid_pairs(n, edges))

