
def f1(n, edges):
    # Calculate the sum of the weights of all except null edge-induced subgraphs of the given tree
    sum_weights = 0
    
    # Iterate over all possible subsets of edges
    for subset in range(2**(n-1)):
        # Convert the binary representation of the subset to a list of edges
        subset_edges = []
        for i in range(n-1):
            if subset & (1 << i):
                subset_edges.append((i+1, i+2))
        
        # Check if the subset forms a tree
        if len(subset_edges) == n-1 and all(e[0] != e[1] for e in subset_edges):
            # Calculate the weight of the subset
            weight = 0
            for i in range(n):
                # Check if the vertex is in the subset
                if subset & (1 << (i-1)):
                    # Count the number of vertices in the subset that are not adjacent to the current vertex
                    count = 0
                    for j in range(n):
                        if j != i and (subset & (1 << (j-1))):
                            count += 1
                    
                    # Add the number of vertices in the subset that are not adjacent to the current vertex to the weight
                    weight += count
            
            # Add the weight to the sum of weights
            sum_weights += weight
    
    return sum_weights % 998244353

def f2(n, edges):
    # Calculate the sum of the weights of all except null edge-induced subgraphs of the given tree
    sum_weights = 0
    
    # Iterate over all possible subsets of edges
    for subset in range(2**(n-1)):
        # Convert the binary representation of the subset to a list of edges
        subset_edges = []
        for i in range(n-1):
            if subset & (1 << i):
                subset_edges.append((i+1, i+2))
        
        # Check if the subset forms a tree
        if len(subset_edges) == n-1 and all(e[0] != e[1] for e in subset_edges):
            # Calculate the weight of the subset
            weight = 0
            for i in range(n):
                # Check if the vertex is in the subset
                if subset & (1 << (i-1)):
                    # Count the number of vertices in the subset that are not adjacent to the current vertex
                    count = 0
                    for j in range(n):
                        if j != i and (subset & (1 << (j-1))):
                            count += 1
                    
                    # Add the number of vertices in the subset that are not adjacent to the current vertex to the weight
                    weight += count
            
            # Add the weight to the sum of weights
            sum_weights += weight
    
    return sum_weights % 998244353

if __name__ == '__main__':
    n = int(input())
    edges = []
    for i in range(n-1):
        u, v = map(int, input().split())
        edges.append((u, v))
    
    print(f1(n, edges))
    print(f2(n, edges))

