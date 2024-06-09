
def is_graph_valid(n, m, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}

    # Add edges to the dictionary
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)

    # Check that the graph is connected
    visited = set()
    queue = [1]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(neighbors[vertex])

    if len(visited) == n:
        return True
    else:
        return False

def find_string(n, m, edges):
    # Initialize a set to store the possible strings
    strings = set()

    # Iterate over the edges of the graph
    for u, v in edges:
        # If the vertices are adjacent, add the corresponding string to the set
        if u == v - 1 or v == u + 1:
            strings.add(chr(u + 96) + chr(v + 96))
        # If the vertices are not adjacent, add all possible strings to the set
        else:
            for i in range(97, 97 + n):
                for j in range(97, 97 + n):
                    if i != j and (i == u + 96 or i == v + 96) and (j == u + 96 or j == v + 96):
                        strings.add(chr(i) + chr(j))

    # Return any string from the set
    return strings.pop()

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    if is_graph_valid(n, m, edges):
        print("Yes")
        print(find_string(n, m, edges))
    else:
        print("No")

