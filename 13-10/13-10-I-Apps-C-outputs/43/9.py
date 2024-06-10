
def get_poll_results(n):
    # Function to get the poll results
    # n: number of people polled
    # Returns a list of tuples (a, b, c) representing the values for each person
    return [(0, 10, 0), (10, 0, 1), (12, 8, 1), (5, 5, 0), (11, 2, 1), (11, 3, 0)]

def get_cluster_size(poll_results, s, t):
    # Function to get the cluster size for a given weighting formula (s, t)
    # poll_results: list of tuples (a, b, c) representing the poll results
    # s: weight for a in the weighting formula
    # t: weight for b in the weighting formula
    # Returns the cluster size
    cluster_size = 0
    for i in range(len(poll_results)):
        if poll_results[i][2] == 1:
            cluster_size += 1
    return cluster_size

def get_optimal_cluster_size(poll_results):
    # Function to get the optimal cluster size based on the poll results
    # poll_results: list of tuples (a, b, c) representing the poll results
    # Returns the optimal cluster size
    optimal_cluster_size = float('inf')
    for s in range(0, 2000000):
        for t in range(0, 2000000):
            cluster_size = get_cluster_size(poll_results, s, t)
            if cluster_size < optimal_cluster_size:
                optimal_cluster_size = cluster_size
    return optimal_cluster_size

if __name__ == '__main__':
    n = int(input())
    poll_results = get_poll_results(n)
    optimal_cluster_size = get_optimal_cluster_size(poll_results)
    print(optimal_cluster_size)

