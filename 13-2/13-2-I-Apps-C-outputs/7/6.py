
def get_smallest_cluster_size(n, a, b, c):
    # Initialize the smallest cluster size
    smallest_cluster_size = float('inf')
    
    # Iterate over all possible values of S and T
    for S in range(0, 2000001):
        for T in range(0, 2000001):
            # Sort the poll results by the measure a_i * S + b_i * T
            sorted_results = sorted(zip(a, b, c), key=lambda x: x[0] * S + x[1] * T)
            
            # Find the indices of the first and last results with c_i true
            j = 0
            k = 0
            for i in range(n):
                if sorted_results[i][2] == 1:
                    j = i
                    break
            for i in range(n-1, -1, -1):
                if sorted_results[i][2] == 1:
                    k = i
                    break
            
            # Calculate the cluster size and update the smallest cluster size if necessary
            cluster_size = k - j + 1
            if cluster_size < smallest_cluster_size:
                smallest_cluster_size = cluster_size
    
    return smallest_cluster_size

