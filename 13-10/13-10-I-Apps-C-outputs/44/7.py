
def get_worlds(n, m):
    # Initialize the graph with two vertices and an edge between them
    graph = {0: {1}, 1: set()}

    # Perform n changes
    for i in range(n):
        # Add a new vertex to the graph
        graph[i + 2] = set()

        # Choose an existing edge (u, v)
        u, v = random.sample(graph.items(), 2)

        # Add two new edges (u, i + 2) and (v, i + 2) to the graph
        graph[u].add(i + 2)
        graph[v].add(i + 2)

    # Return the number of non-similar worlds that can be built
    return len({frozenset(frozenset(edge) for edge in graph.items()) for graph in all_isomorphic_graphs(graph, n + 2)}) % (10**9 + 7)

def all_isomorphic_graphs(graph, n):
    if n == 0:
        yield graph
    else:
        for i in range(n):
            for j in range(i + 1, n):
                if (i, j) in graph:
                    yield from all_isomorphic_graphs({k: graph[k] - {i, j} if k in graph else set() for k in graph}, n - 1)
                    yield from all_isomorphic_graphs({k: graph[k] - {j, i} if k in graph else set() for k in graph}, n - 1)
                    yield from all_isomorphic_graphs({k: graph[k] | {i, j} if k in graph else {i, j} for k in graph}, n - 1)
                    yield from all_isomorphic_graphs({k: graph[k] | {j, i} if k in graph else {j, i} for k in graph}, n - 1)

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_worlds(n, m))

