
def is_graph_valid(n, m, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}

    # Add edges to the graph
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

    return len(visited) == n

def find_string(n, m, edges):
    # Initialize a set to store the possible strings
    strings = set()

    # Iterate over all possible strings of length n
    for string in itertools.product("abc", repeat=n):
        # Initialize a dictionary to store the neighbors of each vertex
        neighbors = {i: set() for i in range(1, n + 1)}

        # Add edges to the graph
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

        # If the graph is connected, add the string to the set of possible strings
        if len(visited) == n:
            strings.add("".join(string))

    # Return any string from the set of possible strings
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

