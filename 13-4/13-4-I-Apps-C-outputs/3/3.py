
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
    # Initialize a set to store the possible letters for each vertex
    letters = {i: set("abc") for i in range(1, n + 1)}

    # Add edges to the graph
    for u, v in edges:
        letters[u] &= letters[v]
        letters[v] &= letters[u]

    # Check that the graph is connected
    visited = set()
    queue = [1]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(neighbors[vertex])

    # If the graph is connected, find a string that corresponds to the graph
    if len(visited) == n:
        string = [""] * (n + 1)
        for i in range(1, n + 1):
            string[i] = list(letters[i])[0]
        return "".join(string)
    else:
        return None

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    if is_graph_valid(n, m, edges):
        string = find_string(n, m, edges)
        if string:
            print("Yes")
            print(string)
        else:
            print("No")
    else:
        print("No")

