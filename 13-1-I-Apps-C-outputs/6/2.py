
def get_k_coloring(N, M, k, P):
    # Initialize a graph with N nodes and M edges
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)
    
    # Function to count the number of k-colorings of a subgraph
    def count_colorings(graph, k, coloring):
        if not graph:
            return 1
        
        # Base case: if the subgraph has only one node, return the number of ways to color it
        if len(graph) == 1:
            return k
        
        # Recursive case: count the number of colorings of the subgraph
        total = 0
        for i in range(k):
            if i not in coloring:
                total += count_colorings(graph[1:], k, coloring | {i})
        return total
    
    # Count the number of k-colorings of the entire graph
    return count_colorings(graph, k, set()) % P

