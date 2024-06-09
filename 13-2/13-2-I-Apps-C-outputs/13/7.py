
def is_graph_exist(n, m, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}

    # Add edges to the dictionary
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
            queue.extend(neighbors[vertex] - visited)

    # If the graph is not connected, return False
    if len(visited) != n:
        return False

    # Initialize a list to store the possible strings
    strings = []

    # Recursively generate all possible strings
    def generate_strings(string, used):
        if len(string) == n:
            strings.append(string)
            return
        for i in range(1, n + 1):
            if i not in used:
                generate_strings(string + chr(i + 96), used | {i})

    generate_strings("", set())

    # Check if any of the generated strings correspond to the given graph
    for string in strings:
        graph = {i: set() for i in range(1, n + 1)}
        for i in range(n - 1):
            if string[i] == string[i + 1]:
                graph[i + 1].add(i + 2)
            elif string[i] == "a" and string[i + 1] == "b":
                graph[i + 1].add(i + 2)
            elif string[i] == "b" and string[i + 1] == "c":
                graph[i + 1].add(i + 2)
        if graph == neighbors:
            return True
    return False

def f1(...):
    ...

def f2(...):
    ...

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    if is_graph_exist(n, m, edges):
        print("Yes")
        print("".join(chr(i + 96) for i in range(1, n + 1)))
    else:
        print("No")

