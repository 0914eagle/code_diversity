
def get_routes(areas, roads):
    routes = []
    for road in roads:
        routes.append((road[0], road[1]))
        routes.append((road[1], road[0]))
    return routes

def get_route_f(p, q, routes, areas):
    min_val = float('inf')
    for route in routes:
        if route[0] == p and route[1] == q:
            min_val = min(min_val, areas[p-1])
        elif route[0] == q and route[1] == p:
            min_val = min(min_val, areas[q-1])
    return min_val

def get_average_f(routes, areas):
    total = 0
    for p in range(1, len(areas)+1):
        for q in range(1, len(areas)+1):
            if p != q:
                total += get_route_f(p, q, routes, areas)
    return total / (len(areas) * (len(areas) - 1))

def main():
    areas = list(map(int, input().split()))
    roads = []
    for i in range(int(input())):
        roads.append(list(map(int, input().split())))
    routes = get_routes(areas, roads)
    print(get_average_f(routes, areas))

if __name__ == '__main__':
    main()

