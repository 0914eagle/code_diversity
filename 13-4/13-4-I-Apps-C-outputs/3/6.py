
def is_graph_valid(n, m, edges):
    # Initialize a graph with n vertices and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Check if the graph is valid
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] == 1 and graph[j][i] == 1:
                return False

    return True

def find_string(n, m, edges):
    # Initialize a set of possible strings
    strings = set()

    # Iterate over all possible strings
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                strings.add(chr(i + 97) + chr(j + 97) + chr(k + 97))

    # Check if any of the strings correspond to the given graph
    for string in strings:
        graph = []
        for i in range(n - 1):
            graph.append([string[i], string[i + 1]])
        if is_graph_valid(n, m, graph):
            return string

    return "No"

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(find_string(n, m, edges))

