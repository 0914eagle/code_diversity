
import math

def calculate_distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def dfs(graph, node, visited, residents, k):
    visited.add(node)
    total_residents = residents[node]
    for neighbor in graph[node]:
        if neighbor not in visited:
            total_residents += dfs(graph, neighbor, visited, residents, k)
    return total_residents

def can_make_happy(graph, residents, k, D):
    visited = set()
    for node in graph:
        if node not in visited:
            total_residents = dfs(graph, node, visited, residents, k)
            if total_residents % k == 0:
                return True
    return False

def binary_search_minimal_D(N, K, cities):
    graph = {i: [] for i in range(N)}
    residents = {}
    for i, city in enumerate(cities):
        x, y, r = city
        residents[i] = r
        for j in range(i):
            distance = calculate_distance(cities[i][:2], cities[j][:2])
            if distance <= D:
                graph[i].append(j)
                graph[j].append(i)
    
    low, high = 0, 10**9
    while high - low > 1e-9:
        mid = (low + high) / 2
        if can_make_happy(graph, residents, K, mid):
            high = mid
        else:
            low = mid
    
    return round(high, 3)

if __name__ == "__main__":
    N, K = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(N)]
    print(binary_search_minimal_D(N, K, cities))
