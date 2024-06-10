
def sort_by_a_times_s_plus_b_times_t(a, b, c, s, t):
    return a * s + b * t

def get_smallest_cluster_size(n, a, b, c):
    smallest_cluster_size = float('inf')
    for s in range(1, 2000001):
        for t in range(1, 2000001):
            sorted_data = sorted(zip(a, b, c), key=lambda x: sort_by_a_times_s_plus_b_times_t(x[0], x[1], x[2], s, t))
            cluster_size = 1
            for i in range(1, n):
                if sorted_data[i][2] == sorted_data[i-1][2]:
                    cluster_size += 1
                else:
                    smallest_cluster_size = min(smallest_cluster_size, cluster_size)
                    cluster_size = 1
            smallest_cluster_size = min(smallest_cluster_size, cluster_size)
    return smallest_cluster_size

def main():
    n = int(input())
    a = []
    b = []
    c = []
    for i in range(n):
        ai, bi, ci = map(int, input().split())
        a.append(ai)
        b.append(bi)
        c.append(ci)
    print(get_smallest_cluster_size(n, a, b, c))

if __name__ == '__main__':
    main()

