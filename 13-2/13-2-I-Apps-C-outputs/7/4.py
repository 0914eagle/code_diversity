
def get_cluster_size(a, b, c):
    # Sort the data by the measure a*S + b*T
    sorted_data = sorted(zip(a, b, c), key=lambda x: x[0]*S + x[1]*T)
    
    # Find the indices of the first and last results with c=1
    j = 0
    k = 0
    for i in range(len(sorted_data)):
        if sorted_data[i][2] == 1:
            j = i
            break
    for i in range(len(sorted_data)-1, -1, -1):
        if sorted_data[i][2] == 1:
            k = i
            break
    
    # Return the cluster size
    return k-j+1

def solve(n, a, b, c):
    # Initialize the smallest cluster size
    smallest_cluster_size = float('inf')
    
    # Iterate over all possible values of S and T
    for S in range(100):
        for T in range(100):
            # Get the cluster size for this (S, T) pair
            cluster_size = get_cluster_size(a, b, c)
            
            # Update the smallest cluster size
            if cluster_size < smallest_cluster_size:
                smallest_cluster_size = cluster_size
    
    # Return the smallest cluster size
    return smallest_cluster_size

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    print(solve(n, a, b, c))

