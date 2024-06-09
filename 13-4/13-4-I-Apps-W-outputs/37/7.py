
def f1(n, edges):
    # Calculate the number of independent sets in the graph
    num_independent_sets = 0
    
    # Iterate over all possible subsets of vertices
    for subset in range(1 << n):
        # Check if the current subset is an independent set
        if is_independent_set(subset, edges):
            num_independent_sets += 1
    
    return num_independent_sets

def f2(n, edges):
    # Calculate the sum of the number of independent sets in all edge-induced subgraphs
    sum_independent_sets = 0
    
    # Iterate over all possible subsets of edges
    for subset in range(1 << n):
        # Check if the current subset is a non-empty edge-induced subgraph
        if is_non_empty_edge_induced_subgraph(subset, edges):
            # Calculate the number of independent sets in the current subgraph
            num_independent_sets = f1(n, edges & subset)
            sum_independent_sets += num_independent_sets
    
    return sum_independent_sets

def is_independent_set(subset, edges):
    # Check if the current subset is an independent set
    for i in range(n):
        for j in range(i+1, n):
            if (subset >> i) & 1 and (subset >> j) & 1 and (edges >> (i*n+j)) & 1:
                return False
    return True

def is_non_empty_edge_induced_subgraph(subset, edges):
    # Check if the current subset is a non-empty edge-induced subgraph
    return subset > 0 and (subset & (subset - 1)) == 0

if __name__ == '__main__':
    n = int(input())
    edges = 0
    for i in range(n-1):
        u, v = map(int, input().split())
        edges |= 1 << (u*n+v)
    print(f2(n, edges) % 998244353)

