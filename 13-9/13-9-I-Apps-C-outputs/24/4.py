
def solve(n, data):
    # convert the data to a list of tuples (a, b, c)
    data = [(a, b, c) for a, b, c in data]

    # find the indices of the first and last results with c=1
    j, k = next((i, j) for i, (a, b, c) in enumerate(data) if c == 1), len(data) - next(j for j, (a, b, c) in enumerate(reversed(data)) if c == 1) - 1

    # initialize the smallest possible cluster size
    smallest_cluster_size = k - j + 1

    # try all possible values of S and T
    for S in range(0, 2000001):
        for T in range(0, 2000001):
            # sort the data by the measure a*S + b*T
            sorted_data = sorted(data, key=lambda x: x[0] * S + x[1] * T)

            # find the indices of the first and last results with c=1 in the sorted data
            i, j = next((i, j) for i, (a, b, c) in enumerate(sorted_data) if c == 1), len(sorted_data) - next(j for j, (a, b, c) in enumerate(reversed(sorted_data)) if c == 1) - 1

            # update the smallest possible cluster size
            smallest_cluster_size = min(smallest_cluster_size, j - i + 1)

    return smallest_cluster_size

