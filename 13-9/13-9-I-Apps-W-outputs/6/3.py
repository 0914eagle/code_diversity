
def get_cables(cities, n):
    cables = []
    for i in range(n):
        for j in range(i+1, n):
            if cities[i] != cities[j]:
                cables.append((cities[i], cities[j]))
    return cables

def get_total_length(cables):
    total_length = 0
    for cable in cables:
        total_length += abs(cable[0] - cable[1])
    return total_length

def get_min_total_length(cables, n):
    min_total_length = get_total_length(cables)
    for i in range(n):
        for j in range(i+1, n):
            if cables[i][0] != cables[j][1] and cables[i][1] != cables[j][0]:
                min_total_length = min(min_total_length, get_total_length(cables[:i] + cables[i+1:] + [cables[j]]))
    return min_total_length

def solve(cities):
    n = len(cities)
    cables = get_cables(cities, n)
    return get_min_total_length(cables, n)

if __name__ == '__main__':
    cities = []
    n = int(input())
    for i in range(n):
        x, c = map(int, input().split())
        cities.append(x)
    print(solve(cities))

