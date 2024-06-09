
def solve(n, polls):
    # Sort the polls by the measure a_i * S + b_i * T
    polls.sort(key=lambda x: x[0] * S + x[1] * T)
    
    # Initialize the cluster size to the total number of polls
    cluster_size = n
    
    # Iterate through the polls and find the cluster size
    for i in range(n-1):
        if polls[i][2] == 1 and polls[i+1][2] == 0:
            cluster_size = min(cluster_size, i+1)
    
    return cluster_size

