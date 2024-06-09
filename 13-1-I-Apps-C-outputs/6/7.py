
def get_k_coloring_count(n, m, k, p):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    # Function to count the number of k-colorings of a subgraph
    def count_colorings(graph, k, p):
        if len(graph) == 1:
            return k
        count = 0
        for c in range(k):
            for neighbor in graph[0]:
                if neighbor not in graph:
                    continue
                graph[0].remove(neighbor)
                count += count_colorings(graph, k, p)
                graph[0].append(neighbor)
        return count % p
    
    # Count the number of k-colorings of the entire graph
    return count_colorings(graph, k, p)

