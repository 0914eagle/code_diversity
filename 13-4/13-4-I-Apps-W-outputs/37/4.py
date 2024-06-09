
def f1(n, edges):
    # Calculate the number of independent sets in the graph
    num_independent_sets = 0
    
    # Iterate over all possible subsets of vertices
    for subset in range(1, 2**n):
        # Check if the current subset is an independent set
        if is_independent_set(subset, n, edges):
            num_independent_sets += 1
    
    return num_independent_sets

def f2(n, edges):
    # Calculate the sum of the number of independent sets in all edge-induced subgraphs
    sum_independent_sets = 0
    
    # Iterate over all possible subsets of edges
    for subset in range(1, 2**(n-1)):
        # Check if the current subset is a non-empty edge-induced subgraph
        if is_edge_induced_subgraph(subset, n, edges):
            # Calculate the number of independent sets in the current subgraph
            num_independent_sets = f1(n, edges & subset)
            sum_independent_sets += num_independent_sets
    
    return sum_independent_sets

def is_independent_set(subset, n, edges):
    # Check if the current subset is an independent set
    for i in range(n):
        for j in range(i+1, n):
            if (subset >> i) & 1 and (subset >> j) & 1 and (i, j) in edges:
                return False
    return True

def is_edge_induced_subgraph(subset, n, edges):
    # Check if the current subset is a non-empty edge-induced subgraph
    for i in range(n):
        for j in range(i+1, n):
            if (subset >> i) & 1 and (subset >> j) & 1 and (i, j) not in edges:
                return False
    return True

if __name__ == '__main__':
    n = int(input())
    edges = set()
    
    for i in range(n-1):
        u, v = map(int, input().split())
        edges.add((u, v))
    
    print(f2(n, edges) % 998244353)

