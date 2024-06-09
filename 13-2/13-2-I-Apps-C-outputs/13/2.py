
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

    # Recursive function to generate all possible strings
    def generate_strings(string, index):
        # Base case: if the string is complete, add it to the list of possible strings
        if index == n:
            strings.append(string)
            return

        # Recursive case: try all possible characters at the current index
        for char in "abc":
            # If the character is not a neighbor of the current vertex, skip it
            if char not in neighbors[index + 1]:
                continue

            # Add the character to the string and recurse
            generate_strings(string + char, index + 1)

    # Generate all possible strings
    generate_strings("", 0)

    # Check if any of the possible strings correspond to the given graph
    for string in strings:
        # Initialize a dictionary to store the neighbors of each vertex in the string
        string_neighbors = {i: set() for i in range(1, n + 1)}

        # Add edges to the dictionary
        for i in range(n - 1):
            if string[i] == string[i + 1]:
                string_neighbors[i + 1].add(i + 2)
                string_neighbors[i + 2].add(i + 1)

        # Check if the string graph is connected
        visited = set()
        queue = [1]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                queue.extend(string_neighbors[vertex] - visited)

        # If the string graph is connected, return True
        if len(visited) == n:
            return True

    # If no string corresponds to the given graph, return False
    return False

def main():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print("Yes") if is_graph_exist(n, m, edges) else print("No")

if __name__ == '__main__':
    main()

