
import math

def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def dfs(graph, visited, residents, node, K, total_residents):
    visited[node] = True
    total_residents += residents[node]
    
    for neighbor in graph[node]:
        if not visited[neighbor]:
            total_residents = dfs(graph, visited, residents, neighbor, K, total_residents)
    
    return total_residents

def can_build_roads(graph, residents, D, K):
    visited = [False] * len(graph)
    
    for i in range(len(graph)):
        if not visited[i]:
            total_residents = dfs(graph, visited, residents, i, K, 0)
            if total_residents % K == 0:
                return True
    
    return False

def binary_search_minimal_D(N, K, cities):
    graph = {i: [] for i in range(N)}
    residents = [0] * N
    
    for i, city in enumerate(cities):
        x, y, r = city
        residents[i] = r
        for j in range(i):
            distance = calculate_distance(cities[i][0], cities[i][1], cities[j][0], cities[j][1])
            if distance <= D:
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
