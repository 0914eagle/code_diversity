
def read_input():
    n, m = map(int, input().split())
    areas = list(map(int, input().split()))
    roads = []
    for _ in range(m):
        x, y = map(int, input().split())
        roads.append((x, y))
    return n, m, areas, roads

def find_min_animals(p, q, areas, roads):
    min_animals = float('inf')
    for road in roads:
        if road[0] == p and road[1] == q:
            min_animals = min(min_animals, areas[p - 1], areas[q - 1])
        elif road[0] == q and road[1] == p:
            min_animals = min(min_animals, areas[p - 1], areas[q - 1])
    return min_animals

def calculate_average(n, m, areas, roads):
    total = 0
    for p in range(1, n + 1):
        for q in range(1, n + 1):
            if p != q:
                total += find_min_animals(p, q, areas, roads)
    return total / (n * (n - 1))

if __name__ == '__main__':
    n, m, areas, roads = read_input()
    print(calculate_average(n, m, areas, roads))

