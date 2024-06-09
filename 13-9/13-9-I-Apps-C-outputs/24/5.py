
def get_smallest_cluster_size(n, a, b, c):
    # Initialize the smallest cluster size and the corresponding (S, T) pair
    smallest_cluster_size = float('inf')
    best_st_pair = (0, 0)

    # Iterate over all possible (S, T) pairs
    for s in range(0, 2000001):
        for t in range(0, 2000001):
            # Sort the poll results by the measure a_i * S + b_i * T
            sorted_indices = sorted(range(n), key=lambda i: a[i] * s + b[i] * t)

            # Find the indices of the first and last results with c_i true
            j = 0
            k = 0
            while j < n and not c[sorted_indices[j]]:
                j += 1
            while k < n and c[sorted_indices[k]]:
                k += 1

            # Calculate the cluster size and compare it with the current smallest cluster size
            cluster_size = k - j + 1
            if cluster_size < smallest_cluster_size:
                smallest_cluster_size = cluster_size
                best_st_pair = (s, t)

    return smallest_cluster_size

