
import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def dfs(city, graph, visited, residents, K):
    visited.add(city)
    total_residents = residents[city]
    for neighbor in graph[city]:
        if neighbor not in visited:
            total_residents += dfs(neighbor, graph, visited, residents, K)
    if total_residents % K == 0:
        return total_residents
    return 0

def build_graph(N, cities):
    graph = {i: [] for i in range(N)}
    residents = {}
    for i, city in enumerate(cities):
        residents[i] = city[2]
        for j in range(i + 1, N):
            distance = calculate_distance(city[:2], cities[j][:2])
            if distance <= D:
                graph[i].append(j)
                graph[j].append(i)
    return graph, residents

def binary_search(cities, K):
    low, high = 0, 10**9
    while high - low > 1e-9:
        global D
        D = (low + high) / 2
        graph, residents = build_graph(len(cities), cities)
        visited = set()
        happy = any(dfs(city, graph, visited, residents, K) for city in range(len(cities)) if city not in visited)
        if happy:
            high = D
        else:
            low = D
    return D

if __name__ == "__main__":
    N, K = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(N)]
    print("{:.3f}".format(binary_search(cities, K)))
