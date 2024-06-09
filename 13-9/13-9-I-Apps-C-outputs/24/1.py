
def solve(n, poll_results):
    # Initialize the smallest cluster size
    smallest_cluster_size = float('inf')

    # Iterate over all possible values of S and T
    for S in range(0, 2000001):
        for T in range(0, 2000001):
            # Sort the poll results by the measure a_i * S + b_i * T
            sorted_results = sorted(poll_results, key=lambda x: x[0] * S + x[1] * T)

            # Initialize the current cluster size
            current_cluster_size = 0

            # Iterate over the sorted results and find the cluster size
            for i in range(n):
                if sorted_results[i][2] == 1:
                    current_cluster_size += 1
                else:
                    if current_cluster_size > smallest_cluster_size:
                        smallest_cluster_size = current_cluster_size
                    current_cluster_size = 0

            # Check if the current cluster size is the smallest seen so far
            if current_cluster_size > smallest_cluster_size:
                smallest_cluster_size = current_cluster_size

    return smallest_cluster_size

