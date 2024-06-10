
def get_input():
    k, n = map(int, input().split())
    a = list(map(int, input().split()))
    return k, n, a

def get_distances(k, n, a):
    distances = []
    for i in range(n):
        distance = a[i]
        if i > 0:
            distance = min(distance, k - a[i-1])
        if i < n-1:
            distance = min(distance, a[i+1] - a[i])
        distances.append(distance)
    return distances

def get_min_distance(distances):
    return sum(distances)

def main():
    k, n, a = get_input()
    distances = get_distances(k, n, a)
    print(get_min_distance(distances))

if __name__ == '__main__':
    main()

