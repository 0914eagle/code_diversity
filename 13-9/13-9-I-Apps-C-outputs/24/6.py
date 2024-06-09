
def solve(n, a, b, c):
    # find the indices of the first and last person who will vote for Candidate X
    first_index = next((i for i, x in enumerate(c) if x == 1), None)
    last_index = next(i for i in range(len(c)-1, -1, -1) if c[i] == 1)

    # initialize the smallest cluster size to a large value
    smallest_cluster_size = float('inf')

    # try all possible values of S and T
    for S in range(0, 2000001):
        for T in range(0, 2000001):
            # sort the poll results by the measure a_i * S + b_i * T
            sorted_results = sorted(zip(a, b, c), key=lambda x: x[0] * S + x[1] * T)

            # find the indices of the first and last person with c_i == 1 in the sorted results
            first_index_sorted = next((i for i, x in enumerate(sorted_results) if x[2] == 1), None)
            last_index_sorted = next(i for i in range(len(sorted_results)-1, -1, -1) if sorted_results[i][2] == 1)

            # calculate the cluster size and update the smallest cluster size if necessary
            cluster_size = last_index_sorted - first_index_sorted + 1
            if cluster_size < smallest_cluster_size:
                smallest_cluster_size = cluster_size

    return smallest_cluster_size

