
def get_cable_length(city1, city2):
    return abs(city1 - city2)

def get_min_cable_length(cities):
    n = len(cities)
    if n == 1:
        return 0
    if n == 2:
        return get_cable_length(cities[0], cities[1])
    
    mid = n // 2
    left_cables = get_min_cable_length(cities[:mid])
    right_cables = get_min_cable_length(cities[mid:])
    merged_cables = 0
    i, j = 0, mid
    while i < mid and j < n:
        if cities[i] < cities[j]:
            i += 1
        elif cities[i] > cities[j]:
            j += 1
        else:
            merged_cables += get_cable_length(cities[i], cities[j])
            i += 1
            j += 1
    
    return left_cables + right_cables + merged_cables

def get_total_cost(cities, type):
    n = len(cities)
    total_cost = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if cities[i][1] == type and cities[j][1] == type:
                total_cost += get_cable_length(cities[i][0], cities[j][0])
    return total_cost

def get_min_total_cost(cities):
    n = len(cities)
    min_total_cost = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            total_cost = get_total_cost(cities[:i] + cities[j:], cities[i][1]) + get_total_cost(cities[i:j] + cities[j:], cities[j][1])
            min_total_cost = min(min_total_cost, total_cost)
    return min_total_cost

def main():
    n = int(input())
    cities = []
    for i in range(n):
        x, type = map(int, input().split())
        cities.append((x, type))
    print(get_min_total_cost(cities))

if __name__ == '__main__':
    main()

