
import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def dfs(graph, city, visited, residents, k):
    visited.add(city)
    total_residents = residents[city]
    for neighbor in graph[city]:
        if neighbor not in visited:
            total_residents += dfs(graph, neighbor, visited, residents, k)
    return total_residents

def can_make_happy(graph, residents, k, D):
    visited = set()
    for city in graph:
        if city not in visited:
            total_residents = dfs(graph, city, visited, residents, k)
            if total_residents % k == 0:
                return True
    return False

def find_minimal_D(N, K, cities):
    graph = {i: [] for i in range(N)}
    residents = {}
    for i, city in enumerate(cities):
        residents[i] = city[2]
        for j in range(i):
            distance = calculate_distance(city, cities[j])
            if distance <= D:
                graph[i].append(j)
                graph[j].append(i)
    
    left, right = 0, 10**9
    while right - left > 1e-9:
        mid = (left + right) / 2
        if can_make_happy(graph, residents, K, mid):
            right = mid
        else:
            left = mid
    
    return round(right, 3)

if __name__ == "__main__":
    N, K = map(int, input().split())
    cities = [list(map(int, input().split())) for _ in range(N)]
    print(find_minimal_D(N, K, cities))
