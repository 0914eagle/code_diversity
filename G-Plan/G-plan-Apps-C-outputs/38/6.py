
import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def dfs(graph, visited, node, residents, K):
    visited[node] = True
    total_residents = residents[node]
    for neighbor in graph[node]:
        if not visited[neighbor]:
            total_residents += dfs(graph, visited, neighbor, residents, K)
    return total_residents

def can_build_roads(graph, residents, D, K):
    visited = [False] * len(graph)
    for i in range(len(graph)):
        if not visited[i]:
            total_residents = dfs(graph, visited, i, residents, K)
            if total_residents % K == 0:
                return True
    return False

def binary_search_minimal_D(N, K, cities):
    graph = [[] for _ in range(N)]
    residents = [0] * N
    for i, (x, y, r) in enumerate(cities):
        residents[i] = r
        for j in range(i):
            dist = calculate_distance(cities[i][:2], cities[j][:2])
            if dist <= D:
                graph[i].append(j)
                graph[j].append(i)

    low, high = 0, 10**9
    while high - low > 1e-9:
        D = (low + high) / 2
        if can_build_roads(graph, residents, D, K):
            high = D
        else:
            low = D
    return round(D, 3)

if __name__ == "__main__":
    N, K = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(N)]
    print(binary_search_minimal_D(N, K, cities))
