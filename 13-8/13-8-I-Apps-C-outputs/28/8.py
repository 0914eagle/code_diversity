
def solve(n, m, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}

    # Add the edges to the dictionary
    for edge in edges:
        u, v = edge[0], edge[1]
        neighbors[u].add(v)
        neighbors[v].add(u)

    # Check if the graph is connected
    visited = set()
    queue = [1]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(neighbors[vertex] - visited)

    if len(visited) == n:
        # The graph is connected, now find a possible string
        s = ["a"] * n
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                if j in neighbors[i]:
                    s[j - 1] = "b"
                    break
            else:
                s[j - 1] = "c"

        # Check if the string produces the given graph
        for i in range(n - 1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    return "Yes\n" + "".join(s)

                if s[i] == "a" and s[j] == "c":
                    return "No"

        return "Yes\n" + "".join(s)

    else:
        return "No"

