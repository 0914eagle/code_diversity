
def check_graph(n, m, edges):
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

    if len(visited) == n:
        return True
    else:
        return False

def find_string(n, m, edges):
    # Initialize a set to store the possible strings
    strings = set()

    # Iterate over the edges and add the corresponding letters to the set of possible strings
    for u, v in edges:
        if u == v - 1:
            strings.add("a" + "b" * (v - 1))
        elif u == v + 1:
            strings.add("b" + "a" * (v - 1))
        else:
            strings.add("a" * (v - 1) + "c" + "b" * (n - v))

    # Check if the graph is connected with the possible strings
    for string in strings:
        if check_graph(n, m, [(i, i + 1) for i in range(n - 1)]):
            return string

    return "No"

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(find_string(n, m, edges))

