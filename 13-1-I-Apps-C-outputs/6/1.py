
def get_k_colorings(N, M, k, P):
    # Initialize a graph with N nodes and M edges
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    # Function to count k-colorings of a subgraph
    def count_colorings(graph, k, P):
        if len(graph) == 1:
            return k
        count = 0
        for i in range(k):
            for j in range(k):
                if i != j:
                    count += count_colorings(graph[1:], k, P)
        return count % P
    
    # Count k-colorings of the entire graph
    return count_colorings(graph, k, P)

