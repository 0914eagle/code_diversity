
def count_valid_pairs(n, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}

    # Add edges to the dictionary
    for edge in edges:
        neighbors[edge[0]].add(edge[1])
        neighbors[edge[1]].add(edge[0])

    # Initialize a set to store the valid pairs
    valid_pairs = set()

    # Iterate over all possible pairs of vertices
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

        # If the vertex has already been visited, continue
        if vertex in visited:
            continue

        # Mark the vertex as visited
        visited.add(vertex)

        # Add the neighbors of the vertex to the stack
        for neighbor in neighbors[vertex]:
            stack.append(neighbor)

        # If a 1-edge has been encountered and a 0-edge is encountered, return False
        if one_edge_encountered and not is_one_edge(neighbors, vertex, j):
            return False

        # If a 1-edge is encountered, set the flag to True
        if is_one_edge(neighbors, vertex, j):
            one_edge_encountered = True

    # If the destination vertex is not in the visited set, return False
    return j in visited

def is_one_edge(neighbors, vertex, destination):
    # Initialize a flag to indicate if a 1-edge has been encountered
    one_edge_encountered = False

    # Iterate over the neighbors of the vertex
    for neighbor in neighbors[vertex]:
        # If the neighbor is the destination vertex, return True
        if neighbor == destination:
            return True

        # If a 1-edge has been encountered and a 0-edge is encountered, return False
        if one_edge_encountered and not is_one_edge(neighbors, neighbor, destination):
            return False

        # If a 1-edge is encountered, set the flag to True
        if is_one_edge(neighbors, neighbor, destination):
            one_edge_encountered = True

    # If the destination vertex is not in the neighbors of the vertex, return False
    return destination in neighbors[vertex]

n = int(input())
edges = []
for i in range(n - 1):
    x, y, c = map(int, input().split())
    edges.append((x, y, c))

print(count_valid_pairs(n, edges))

