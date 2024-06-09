
def is_graph_reconstructable(n, m, edges):
    # Initialize a dictionary to store the neighbors of each vertex
    neighbors = {i: set() for i in range(1, n + 1)}

    # Add edges to the graph
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
    def generate_strings(string, index):
        if index == n:
            strings.append(string)
            return
        for char in "abc":
            generate_strings(string + char, index + 1)

    generate_strings("", 0)

    # Check if any of the generated strings correspond to the given graph
    for string in strings:
        graph = {}
        for i in range(n):
            graph[i + 1] = set(string[i])
        if all(graph[u].intersection(graph[v]) for u, v in edges):
            return True, string
    return False, None

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    result = is_graph_reconstructable(n, m, edges)
    if result[0]:
        print("Yes")
        print(result[1])
    else:
        print("No")

if __name__ == '__main__':
    main()

