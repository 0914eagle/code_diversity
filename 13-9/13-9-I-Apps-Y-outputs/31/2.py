
def solve(n, m, roads):
    city_roads = [0] * (n + 1)
    for road in roads:
        city_roads[road[0]] += 1
        city_roads[road[1]] += 1
    return city_roads[1:]

