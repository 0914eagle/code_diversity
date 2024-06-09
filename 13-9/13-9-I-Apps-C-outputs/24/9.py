
def solve(n, a, b, c):
    # find the indices of the first and last person who will vote for Candidate X
    j = 0
    k = 0
    for i in range(n):
        if c[i] == 1:
            j = i
            break
    for i in range(n-1, -1, -1):
        if c[i] == 1:
            k = i
            break
    
    # initialize the smallest cluster size and the corresponding S and T values
    smallest_cluster_size = k-j+1
    smallest_S = 0
    smallest_T = 0
    
    # iterate over all possible S and T values
    for S in range(0, 2000001):
        for T in range(0, 2000001):
            # sort the poll results by the measure a_i * S + b_i * T
            sorted_results = sorted(zip(a, b, c), key=lambda x: x[0]*S + x[1]*T)
            
            # find the indices of the first and last person with c_i true in the sorted results
            j_sorted = 0
            k_sorted = 0
            for i in range(n):
                if sorted_results[i][2] == 1:
                    j_sorted = i
                    break
            for i in range(n-1, -1, -1):
                if sorted_results[i][2] == 1:
                    k_sorted = i
                    break
                    
            # calculate the cluster size for this (S, T) pair
            cluster_size = k_sorted - j_sorted + 1
            
            # if the cluster size is smaller than the smallest cluster size found so far, update the smallest cluster size and the corresponding S and T values
            if cluster_size < smallest_cluster_size:
                smallest_cluster_size = cluster_size
                smallest_S = S
                smallest_T = T
    
    return smallest_cluster_size

