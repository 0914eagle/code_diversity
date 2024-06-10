
def get_route_cost(route, areas):
    cost = 0
    for i in range(len(route) - 1):
        cost += min(areas[route[i]], areas[route[i + 1]])
    return cost

def get_all_routes(n):
    routes = []
    for i in range(n):
        for j in range(i + 1, n):
            routes.append([i, j])
    return routes

def get_average_route_cost(areas, roads):
    n = len(areas)
    routes = get_all_routes(n)
    total_cost = 0
    for route in routes:
        cost = get_route_cost(route, areas)
        total_cost += cost
    return total_cost / (n * (n - 1))

def main():
    n, m = map(int, input().split())
    areas = list(map(int, input().split()))
    roads = []
    for i in range(m):
        x, y = map(int, input().split())
        roads.append([x, y])
    print(get_average_route_cost(areas, roads))

if __name__ == '__main__':
    main()

