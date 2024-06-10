
def get_input():
    n, m = map(int, input().split())
    areas = list(map(int, input().split()))
    roads = []
    for _ in range(m):
        x, y = map(int, input().split())
        roads.append((x, y))
    return n, m, areas, roads

def get_f(p, q, areas, roads):
    min_value = float('inf')
    for road in roads:
        if road[0] == p and road[1] == q:
            min_value = min(min_value, areas[road[0]-1])
        elif road[0] == q and road[1] == p:
            min_value = min(min_value, areas[road[1]-1])
    return min_value

def get_average(n, m, areas, roads):
    total = 0
    for p in range(1, n+1):
        for q in range(1, n+1):
            if p != q:
                total += get_f(p, q, areas, roads)
    return total / (n * (n-1))

def main():
    n, m, areas, roads = get_input()
    print(get_average(n, m, areas, roads))

if __name__ == '__main__':
    main()

