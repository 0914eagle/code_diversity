
import heapq

def dijkstra(adj_list, start):
    n = len(adj_list)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj_list[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist

N, M, alpha = map(int, input().split())
adj_list = [[] for _ in range(N)]
roads = []

for _ in range(M):
    u, v, c = map(int, input().split())
    adj_list[u-1].append((v-1, c))
    adj_list[v-1].append((u-1, c))
    roads.append((u-1, v-1, c))

min_energy = float('inf')

for u, v, c in roads:
    dist_from_u = dijkstra(adj_list, u)
    dist_from_v = dijkstra(adj_list, v)
    for i in range(N):
        if dist_from_u[i] + dist_from_v[i] + c < min_energy:
            min_energy = dist_from_u[i] + dist_from_v[i] + c

if min_energy == float('inf'):
    print("Poor girl")
else:
    print(min_energy + alpha)

