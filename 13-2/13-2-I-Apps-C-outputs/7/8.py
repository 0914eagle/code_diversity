
def get_cluster_size(a, b, c):
    # Find the indices of the first and last results with c true
    j = next((i for i, x in enumerate(c) if x), None)
    k = next((i for i in range(len(c)-1, -1, -1) if c[i]), None)
    return k-j+1

def get_smallest_cluster_size(a, b, c):
    # Find the smallest possible cluster size over all possible (S, T) pairs
    smallest_cluster_size = float('inf')
    for S in range(0, 2000001):
        for T in range(0, 2000001):
            cluster_size = get_cluster_size(a, b, c)
            if cluster_size < smallest_cluster_size:
                smallest_cluster_size = cluster_size
    return smallest_cluster_size

def main():
    n = int(input())
    a = []
    b = []
    c = []
    for _ in range(n):
        ai, bi, ci = map(int, input().split())
        a.append(ai)
        b.append(bi)
        c.append(ci)
    print(get_smallest_cluster_size(a, b, c))

if __name__ == '__main__':
    main()

