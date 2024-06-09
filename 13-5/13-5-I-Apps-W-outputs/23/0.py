
def read_input():
    n, m, s = map(int, input().split())
    people = list(map(int, input().split()))
    roads = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        roads.append((u, v, w))
    shelters = []
    for _ in range(s):
        s_i, c_i = map(int, input().split())
        shelters.append((s_i, c_i))
    return n, m, s, people, roads, shelters

def dijkstra(graph, source):
    dist = [float('inf')] * len(graph)
    dist[source] = 0
    visited = [False] * len(graph)
    pq = [(0, source)]
    while pq:
        d, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def assign_shelters(n, m, s, people, roads, shelters):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))
    dist = dijkstra(graph, 1)
    assigned_shelters = [0] * (n + 1)
    for i in range(1, n + 1):
        min_dist = float('inf')
        min_shelter = 0
        for j in range(s):
            if dist[i] + people[j] <= shelters[j][1]:
                if dist[i] < min_dist:
                    min_dist = dist[i]
                    min_shelter = j
        assigned_shelters[i] = min_shelter
    return assigned_shelters

def solve(n, m, s, people, roads, shelters):
    assigned_shelters = assign_shelters(n, m, s, people, roads, shelters)
    min_time = 0
    for i in range(1, n + 1):
        min_time += dist[i]
    return min_time

if __name__ == '__main__':
    n, m, s, people, roads, shelters = read_input()
    print(solve(n, m, s, people, roads, shelters))

