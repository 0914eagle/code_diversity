
def get_k_coloring(N, M, k, P):
    # Initialize a graph with N nodes and M edges
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    # Function to count the number of k-colorings of a subgraph
    def count_colorings(subgraph, coloring):
        if not subgraph:
            return 1
        
        count = 0
        for node in subgraph:
            for color in range(k):
                if color not in coloring[node]:
                    coloring[node].add(color)
                    count += count_colorings(subgraph - {node}, coloring)
                    coloring[node].remove(color)
        return count % P
    
    # Function to get the number of k-colorings of the entire graph
    def get_total_colorings():
        coloring = [set() for _ in range(N)]
        return count_colorings(set(range(N)), coloring)
    
    return get_total_colorings()

