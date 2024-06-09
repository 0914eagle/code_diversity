
def get_cluster_size(a, b, c):
    # Find the indices of the first and last results with c_i true
    j = next((i for i, x in enumerate(c) if x), None)
    k = next((i for i in range(len(c)-1, -1, -1) if c[i]), None)
    return k-j+1

def solve(n, a, b, c):
    # Initialize the smallest cluster size
    smallest_cluster_size = float('inf')

    # Iterate over all possible values of S and T
    for S in range(0, 2000001):
        for T in range(0, 2000001):
            # Sort the poll results by the measure a_i * S + b_i * T
            sorted_results = sorted(zip(a, b, c), key=lambda x: x[0] * S + x[1] * T)

            # Get the cluster size for this (S, T) pair
            cluster_size = get_cluster_size(sorted_results)

            # Update the smallest cluster size if necessary
            if cluster_size < smallest_cluster_size:
                smallest_cluster_size = cluster_size

    return smallest_cluster_size

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(solve(n, a, b, c))

