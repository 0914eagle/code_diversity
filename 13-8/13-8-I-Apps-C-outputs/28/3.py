
def solve(n, m, edges):
    # Initialize a dictionary to store the edges
    graph = {}

    # Iterate over the edges and add them to the dictionary
    for edge in edges:
        u, v = edge[0], edge[1]
        if u not in graph:
            graph[u] = [v]
        else:
            graph[u].append(v)

    # Initialize a list to store the possible strings
    strings = []

    # Iterate over the vertices and find the possible strings
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if i == j:
                continue
            if j in graph[i]:
                strings.append("a" * (j - i) + "b" + "c" * (n - j))
            else:
                strings.append("a" * (j - i) + "c" * (n - j))

    # Check if any of the possible strings form the original graph
    for string in strings:
        if len(string) != n:
            continue
        graph_string = {}
        for i in range(n - 1):
            if string[i] == string[i + 1]:
                if i not in graph_string:
                    graph_string[i] = [i + 1]
                else:
                    graph_string[i].append(i + 1)
            elif string[i] == "b" and string[i + 1] == "c":
                if i not in graph_string:
                    graph_string[i] = [i + 1]
                else:
                    graph_string[i].append(i + 1)
        if graph_string == graph:
            return "Yes\n" + string

    return "No"

