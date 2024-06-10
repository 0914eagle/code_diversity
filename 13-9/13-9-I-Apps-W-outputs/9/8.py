
def get_max_distance(n, x, a, b):
    if a == b:
        return 0
    if x == 0:
        return abs(a - b)
    if a > b:
        a, b = b, a
    distance = b - a
    for i in range(a + 1, b):
        distance = max(distance, abs(i - a), abs(i - b))
    return distance

def get_max_distance_brute_force(n, x, a, b):
    if a == b:
        return 0
    if x == 0:
        return abs(a - b)
    distances = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if i != a and j != b:
                distances.append(abs(i - j))
    return max(distances)

def get_max_distance_brute_force_optimized(n, x, a, b):
    if a == b:
        return 0
    if x == 0:
        return abs(a - b)
    distances = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if i != a and j != b:
                distances.append(abs(i - j))
    return max(distances)

def main():
    t = int(input())
    for _ in range(t):
        n, x, a, b = map(int, input().split())
        print(get_max_distance(n, x, a, b))

if __name__ == '__main__':
    main()

