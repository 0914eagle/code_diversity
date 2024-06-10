
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

def can_build_roads(graph, residents, k, d):
    visited = set()
    for node in graph:
        if node not in visited:
            total_residents = dfs(graph, node, visited, residents, k)
            if total_residents % k == 0:
                return True
    return False

def binary_search_minimal_d(cities, k):
    def build_graph(cities, d):
        graph = {i: [] for i in range(len(cities))}
        for i in range(len(cities)):
            for j in range(i + 1, len(cities)):
                if calculate_distance(cities[i][:2], cities[j][:2]) <= d:
                    graph[i].append(j)
                    graph[j].append(i)
        return graph

    def get_residents(cities):
        return {i: city[2] for i, city in enumerate(cities)}

    low, high = 0, 10**9
    while low + 10**-6 < high:
        mid = (low + high) / 2
        graph = build_graph(cities, mid)
        residents = get_residents(cities)
        if can_build_roads(graph, residents, k, mid):
            high = mid
        else:
            low = mid
    return round(high, 3)

if __name__ == "__main__":
    n, k = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(n)]
    print(binary_search_minimal_d(cities, k))
