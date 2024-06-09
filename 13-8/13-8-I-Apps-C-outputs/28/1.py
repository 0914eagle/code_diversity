
def solve(n, m, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}

    # Add the edges to the dictionary
    for u, v in edges:
        neighbors[u].add(v)
        neighbors[v].add(u)

    # Check if the graph is connected
    visited = set()
    queue = [1]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(neighbors[vertex])

    if len(visited) == n:
        # The graph is connected, now find the string
        string = ["a"] * n
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                if j in neighbors[i]:
                    string[i - 1] = "b"
                    string[j - 1] = "c"
                    break
        return "Yes\n" + "".join(string)
    else:
        return "No"

