
def read_input():
    N = int(input())
    cities = []
    for i in range(N):
        y, d, r = map(int, input().split())
        cities.append((y, d, r))
    return N, cities

def dijkstra(start, cities):
    dist = [float('inf')] * len(cities)
    dist[start] = 0
    visited = [False] * len(cities)
    visited[start] = True
    while True:
        min_dist = float('inf')
        min_index = -1
        for i in range(len(cities)):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                min_index = i
        if min_index == -1:
            break
        visited[min_index] = True
        for i in range(len(cities)):
            if not visited[i] and cities[min_index][1] <= abs(cities[min_index][0] - cities[i][0]):
                dist[i] = min(dist[i], dist[min_index] + abs(cities[min_index][0] - cities[i][0]) + cities[min_index][2])
    return dist

def solve(N, cities):
    dist = dijkstra(0, cities)
    return [dist[i] if dist[i] != float('inf') else -1 for i in range(1, len(cities))]

if __name__ == '__main__':
    N, cities = read_input()
    print(*solve(N, cities), sep='\n')

