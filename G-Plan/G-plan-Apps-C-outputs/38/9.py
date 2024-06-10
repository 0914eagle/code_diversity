
import math

def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def dfs(graph, visited, node, residents, k):
    visited[node] = True
    total_residents = residents[node]
    for neighbor in graph[node]:
        if not visited[neighbor]:
            total_residents += dfs(graph, visited, neighbor, residents, k)
    return total_residents

def can_build_roads(graph, residents, d, k):
    visited = [False] * len(graph)
    for i in range(len(graph)):
        if not visited[i]:
            total_residents = dfs(graph, visited, i, residents, k)
            if total_residents % k == 0:
                return True
    return False

def binary_search_minimal_d(graph, residents, k):
    low = 0
    high = 10**9
    while high - low > 1e-9:
        mid = (low + high) / 2
        if can_build_roads(graph, residents, mid, k):
            high = mid
        else:
            low = mid
    return high

if __name__ == "__main__":
    n, k = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(n)]
    graph = [[] for _ in range(n)]
    residents = [0] * n

    for i, city in enumerate(cities):
        residents[i] = city[2]
        for j in range(i):
            if distance(cities[i][:2], cities[j][:2]) <= city[3]:
                graph[i].append(j)
                graph[j].append(i)

    minimal_d = binary_search_minimal_d(graph, residents, k)
    print("{:.3f}".format(minimal_d))
