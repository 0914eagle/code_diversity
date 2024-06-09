
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

    # Initialize a dictionary to store the characters of the string
    chars = {i: None for i in range(1, n + 1)}

    # Fill in the characters of the string
    for u, v in edges:
        if chars[u] is None:
            chars[u] = "a"
        elif chars[u] == "a":
            chars[u] = "b"
        else:
            chars[u] = "c"

        if chars[v] is None:
            chars[v] = "a"
        elif chars[v] == "a":
            chars[v] = "b"
        else:
            chars[v] = "c"

    # Check if the characters form a valid string
    string = "".join(chars[i] for i in range(1, n + 1))
    if not is_valid_string(string):
        return False

    # If the graph and the string are valid, return True and the string
    return True, string

def is_valid_string(string):
    # Check if the string contains only the characters "a", "b", and "c"
    if not all(c in ["a", "b", "c"] for c in string):
        return False

    # Check if the string is a valid permutation of the characters "a", "b", and "c"
    chars = ["a", "b", "c"]
    for c in string:
        if c not in chars:
            return False
        chars.remove(c)

    return True

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    result = is_graph_exist(n, m, edges)
    if result[0]:
        print("Yes")
        print(result[1])
    else:
        print("No")

if __name__ == '__main__':
    main()

