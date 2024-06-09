
def get_input():
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
    dist = [float('inf') for _ in range(len(graph))]
    dist[source] = 0
    visited = [False for _ in range(len(graph))]
    queue = [(0, source)]
    while queue:
        dist_u, u = heapq.heappop(queue)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(queue, (dist[v], v))
    return dist

def assign_shelters(n, m, s, people, roads, shelters):
    graph = [[] for _ in range(n)]
    for u, v, w in roads:
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    dist = dijkstra(graph, 0)
    assigned_shelters = [0] * n
    for i in range(n):
        if people[i] > 0:
            min_dist = float('inf')
            min_shelter = 0
            for j in range(s):
                if shelters[j][1] >= people[i] and dist[shelters[j][0]-1] < min_dist:
                    min_dist = dist[shelters[j][0]-1]
                    min_shelter = j
            assigned_shelters[i] = min_shelter
    return assigned_shelters

def get_time(n, m, s, people, roads, shelters, assigned_shelters):
    graph = [[] for _ in range(n)]
    for u, v, w in roads:
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    dist = dijkstra(graph, 0)
    time = 0
    for i in range(n):
        if people[i] > 0:
            time += dist[i]
            time += shelters[assigned_shelters[i]][1]
    return time

def main():
    n, m, s, people, roads, shelters = get_input()
    assigned_shelters = assign_shelters(n, m, s, people, roads, shelters)
    time = get_time(n, m, s, people, roads, shelters, assigned_shelters)
    print(time)

if __name__ == '__main__':
    main()

