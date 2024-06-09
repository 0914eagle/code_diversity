
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

    return len(visited) == n

def find_string(n, m, edges):
    # Initialize a set to store the possible strings
    strings = set()

    # Iterate over the edges and add the corresponding letters to the set of possible strings
    for u, v in edges:
        if u == v:
            strings.add("a")
        elif u == v - 1:
            strings.add("b")
        elif u == v + 1:
            strings.add("c")
        else:
            return "No"

    # Check if the set of possible strings is valid
    if len(strings) == n and "a" in strings and "b" in strings and "c" in strings:
        return "Yes\n" + "".join(sorted(strings))
    else:
        return "No"

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(find_string(n, m, edges))

