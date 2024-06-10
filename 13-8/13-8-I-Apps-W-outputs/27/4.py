
def get_input():
    n, m = map(int, input().split())
    areas = list(map(int, input().split()))
    roads = []
    for _ in range(m):
        x, y = map(int, input().split())
        roads.append((x, y))
    return n, m, areas, roads

def get_route_cost(p, q, areas, roads):
    visited = set()
    queue = [(p, 0)]
    while queue:
        current, cost = queue.pop(0)
        if current == q:
            return cost
        if current in visited:
            continue
        visited.add(current)
        for road in roads:
            if road[0] == current:
                queue.append((road[1], cost + areas[road[1] - 1]))
            elif road[1] == current:
                queue.append((road[0], cost + areas[road[0] - 1]))
    return -1

def get_avg_route_cost(n, m, areas, roads):
    total_cost = 0
    for p in range(1, n + 1):
        for q in range(1, n + 1):
            if p != q:
                cost = get_route_cost(p, q, areas, roads)
                total_cost += cost
    return total_cost / (n * (n - 1))

def main():
    n, m, areas, roads = get_input()
    print(get_avg_route_cost(n, m, areas, roads))

if __name__ == '__main__':
    main()

