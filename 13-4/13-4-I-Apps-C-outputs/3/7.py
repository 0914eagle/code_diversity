
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

    # Iterate over all possible strings
    for string in itertools.product("abc", repeat=n):
        # Convert the string to a list of integers
        string_list = [ord(char) - ord("a") + 1 for char in string]

        # Check if the string is a valid solution
        if check_graph(n, m, zip(string_list, string_list[1:])):
            strings.add("".join(string))

    # Return any of the possible strings
    return strings

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print("Yes") if find_string(n, m, edges) else print("No")

