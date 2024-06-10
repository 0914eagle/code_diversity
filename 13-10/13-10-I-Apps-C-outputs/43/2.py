
def get_data():
    n = int(input())
    data = []
    for i in range(n):
        a, b, c = map(int, input().split())
        data.append((a, b, c))
    return data

def get_cluster_size(data):
    cluster_size = 0
    for i in range(len(data)):
        if data[i][2] == 1:
            cluster_size += 1
    return cluster_size

def get_best_cluster_size(data):
    best_cluster_size = float('inf')
    for s in range(0, 2000001):
        for t in range(0, 2000001):
            data_sorted = sorted(data, key=lambda x: x[0] * s + x[1] * t)
            cluster_size = get_cluster_size(data_sorted)
            if cluster_size < best_cluster_size:
                best_cluster_size = cluster_size
    return best_cluster_size

def main():
    data = get_data()
    print(get_best_cluster_size(data))

if __name__ == '__main__':
    main()

