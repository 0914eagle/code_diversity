
def solve(n, files):
    # Initialize a graph with n nodes
    graph = [[] for _ in range(n)]

    # Populate the graph with edges
    for i, file in enumerate(files):
        name, k = file[0], int(file[1])
        for j in range(2, len(file)):
            graph[i].append(file[j].split(", ")[1])

    # Find a shortest cycle in the graph
    cycle = []
    for i in range(n):
        if graph[i]:
            cycle = find_cycle(graph, i)
            if cycle:
                break

    # If there is no cycle, return "SHIP IT"
    if not cycle:
        return "SHIP IT"

    # Otherwise, return the names of the files in the cycle
    return " ".join(cycle)

def find_cycle(graph, node):
    visited = set()
    stack = [node]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
        else:
            return graph[node]
    return []

