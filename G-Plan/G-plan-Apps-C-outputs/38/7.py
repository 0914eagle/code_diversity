
import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def dfs(graph, city, visited, residents, K, total_residents):
    visited[city] = True
    total_residents += residents[city]
    for neighbor in graph[city]:
        if not visited[neighbor]:
            if total_residents % K == 0:
                return True
            if dfs(graph, neighbor, visited, residents, K, total_residents):
                return True
    return False

def build_graph(N, cities):
    graph = {i: [] for i in range(N)}
    for i in range(N):
        for j in range(i + 1, N):
            distance = calculate_distance(cities[i][:2], cities[j][:2])
            if distance <= D:
                graph[i].append(j)
                graph[j].append(i)
    return graph

def binary_search(cities, N, K):
    low, high = 0, 10**9
    while high - low > 1e-9:
        global D
        D = (low + high) / 2
        graph = build_graph(N, cities)
        visited = [False] * N
        residents = [city[2] for city in cities]
        if any(dfs(graph, i, visited, residents, K, 0) for i in range(N)):
            high = D
        else:
            low = D
    return D

if __name__ == "__main__":
    N, K = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(N)]
    print("{:.3f}".format(binary_search(cities, N, K)))
