
def solve(n, a, b, c):
    # Initialize the smallest cluster size
    smallest_cluster_size = float('inf')
    
    # Loop over all possible values of S and T
    for S in range(0, 2000001):
        for T in range(0, 2000001):
            # Sort the poll results by the measure a_i * S + b_i * T
            sorted_results = sorted(zip(a, b, c), key=lambda x: x[0] * S + x[1] * T)
            
            # Initialize the current cluster size
            current_cluster_size = 0
            
            # Loop over the sorted results
            for i in range(n):
                # If the current result has c_i true, increment the current cluster size
                if sorted_results[i][2] == 1:
                    current_cluster_size += 1
                # If the current result has c_i false, check if the current cluster size is smaller than the smallest cluster size
                elif current_cluster_size < smallest_cluster_size:
                    smallest_cluster_size = current_cluster_size
                    break
                # Reset the current cluster size
                else:
                    current_cluster_size = 0
    
    # Return the smallest cluster size
    return smallest_cluster_size

