
def get_non_similar_worlds(n, m):
    # Initialize the graph with only the s and t vertices
    graph = {s: set(), t: set()}

    # Iterate over the number of changes
    for i in range(n):
        # Add a new vertex to the graph
        w = i + 2
        graph[w] = set()

        # Choose an edge (u, v) at random and add the two new edges (u, w) and (v, w)
        u, v = random.sample(graph, 2)
        graph[u].add(w)
        graph[v].add(w)
        graph[w].add(u)
        graph[w].add(v)

    # Count the number of non-similar worlds
    non_similar_worlds = 0
    for u in graph:
        for v in graph:
            if u != v and graph[u] == graph[v]:
                non_similar_worlds += 1

    return non_similar_worlds % (10**9 + 7)

