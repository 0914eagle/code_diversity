
def solve(n, a, b, c):
    # find the indices of the first and last people who will vote for Candidate X
    first_index = next((i for i, x in enumerate(c) if x == 1), None)
    last_index = next(i for i in range(len(c)-1, -1, -1) if c[i] == 1)
    
    # calculate the cluster size for each possible combination of S and T
    cluster_sizes = []
    for s in range(0, 2000001):
        for t in range(0, 2000001):
            # sort the data by the measure a*s + b*t
            sorted_data = sorted(zip(a, b, c), key=lambda x: x[0]*s + x[1]*t)
            
            # find the indices of the first and last people who will vote for Candidate X in the sorted data
            first_index_sorted = next((i for i, x in enumerate(sorted_data) if x[2] == 1), None)
            last_index_sorted = next(i for i in range(len(sorted_data)-1, -1, -1) if sorted_data[i][2] == 1)
            
            # calculate the cluster size for this combination of S and T
            cluster_size = last_index_sorted - first_index_sorted + 1
            cluster_sizes.append(cluster_size)
    
    # return the smallest possible cluster size
    return min(cluster_sizes)

