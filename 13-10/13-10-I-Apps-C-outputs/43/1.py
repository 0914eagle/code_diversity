
def get_cluster_size(a, b, c, s, t):
    # Sort the poll results by the measure a*s + b*t
    sorted_results = sorted(zip(a, b, c), key=lambda x: x[0]*s + x[1]*t)
    
    # Find the first and last indices with c=1
    first_idx = next((i for i, x in enumerate(sorted_results) if x[2] == 1), None)
    last_idx = next((i for i in range(len(sorted_results)-1, -1, -1) if sorted_results[i][2] == 1), None)
    
    # Return the cluster size
    return last_idx - first_idx + 1

def solve(n):
    # Read the input
    a = []
    b = []
    c = []
    for _ in range(n):
        a_i, b_i, c_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        c.append(c_i)
    
    # Find the smallest possible cluster size over all possible (S, T) pairs
    smallest_cluster_size = float('inf')
    for s in range(1, 21):
        for t in range(1, 21):
            cluster_size = get_cluster_size(a, b, c, s, t)
            if cluster_size < smallest_cluster_size:
                smallest_cluster_size = cluster_size
    
    return smallest_cluster_size

if __name__ == '__main__':
    n = int(input())
    print(solve(n))

