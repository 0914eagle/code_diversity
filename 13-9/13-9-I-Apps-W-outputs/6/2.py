
def get_cable_cost(x1, x2):
    return abs(x1 - x2)

def connect_cities(cities, cable_cost):
    n = len(cities)
    cost = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if cities[i] != cities[j]:
                cost += cable_cost[i][j]
    return cost

def solve(cities, cable_cost):
    n = len(cities)
    cost = connect_cities(cities, cable_cost)
    for i in range(n):
        for j in range(i + 1, n):
            if cities[i] != cities[j]:
                cable_cost[i][j] = 0
                cost_with_removed_city = connect_cities(cities, cable_cost)
                if cost_with_removed_city < cost:
                    cost = cost_with_removed_city
                cable_cost[i][j] = get_cable_cost(cities[i], cities[j])
    return cost

def main():
    n = int(input())
    cities = []
    cable_cost = []
    for i in range(n):
        x, c = map(int, input().split())
        cities.append(x)
        cable_cost.append([])
        for j in range(n):
            if i == j:
                cable_cost[i].append(0)
            else:
                cable_cost[i].append(get_cable_cost(x, cities[j]))
    print(solve(cities, cable_cost))

if __name__ == '__main__':
    main()

