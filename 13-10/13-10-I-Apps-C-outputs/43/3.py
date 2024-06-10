
def get_sorted_results(a, b, c, s, t):
    return sorted(zip(a, b, c), key=lambda x: x[0] * s + x[1] * t)

def get_min_cluster_size(a, b, c):
    sorted_results = get_sorted_results(a, b, c, 1, 1)
    cluster_size = 1
    for i in range(1, len(sorted_results)):
        if sorted_results[i][2] != sorted_results[i-1][2]:
            cluster_size += 1
    return cluster_size

def get_best_s_and_t(a, b, c):
    min_cluster_size = float('inf')
    best_s = 0
    best_t = 0
    for s in range(100):
        for t in range(100):
            cluster_size = get_min_cluster_size(a, b, c, s/100, t/100)
            if cluster_size < min_cluster_size:
                min_cluster_size = cluster_size
                best_s = s
                best_t = t
    return (best_s, best_t)

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
    best_s, best_t = get_best_s_and_t(a, b, c)
    print(get_min_cluster_size(a, b, c, best_s/100, best_t/100))

if __name__ == '__main__':
    main()

