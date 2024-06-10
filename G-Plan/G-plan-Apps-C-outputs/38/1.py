
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
    
    if total_residents % k == 0:
        return total_residents
    return 0

def can_build_roads(graph, residents, d, k):
    visited = set()
    
    for node in graph:
        if node not in visited:
            total_residents = dfs(graph, node, visited, residents, k)
            if total_residents != 0:
                return True
    
    return False

def binary_search_minimal_d(cities, n, k):
    def check_feasibility(d):
        graph = {i: [] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                distance = calculate_distance(cities[i][:2], cities[j][:2])
                if distance <= d:
                    graph[i].append(j)
                    graph[j].append(i)
        
        return can_build_roads(graph, residents, d, k)
    
    residents = {i: cities[i][2] for i in range(n)}
    low, high = 0, 10 ** 9
    
    while high - low > 1e-9:
        mid = (low + high) / 2
        if check_feasibility(mid):
            high = mid
        else:
            low = mid
    
    return round(high, 3)

if __name__ == "__main__":
    n, k = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(n)]
    print(binary_search_minimal_d(cities, n, k))
