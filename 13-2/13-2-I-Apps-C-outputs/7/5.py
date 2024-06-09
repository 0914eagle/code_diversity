
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

def main():
    # Read the input
    n = int(input())
    a = []
    b = []
    c = []
    for i in range(n):
        ai, bi, ci = map(int, input().split())
        a.append(ai)
        b.append(bi)
        c.append(ci)
    
    # Find the smallest possible cluster size over all possible (S, T) pairs
    smallest_cluster_size = float('inf')
    for S in range(100):
        for T in range(100):
            cluster_size = get_cluster_size(a, b, c, S, T)
            if cluster_size < smallest_cluster_size:
                smallest_cluster_size = cluster_size
    
    # Print the smallest possible cluster size
    print(smallest_cluster_size)

if __name__ == '__main__':
    main()

