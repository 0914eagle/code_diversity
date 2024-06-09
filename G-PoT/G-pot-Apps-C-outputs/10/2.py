
import sys
from heapq import heappop, heappush

def dijkstra(adj_list, start, end):
    n = len(adj_list)
    dist = [float('inf')] * n
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, u = heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj_list[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heappush(pq, (dist[v], v))
    
    return dist[end]

def main():
    N, M, alpha = map(int, input().split())
    adj_list = [[] for _ in range(N)]
    
    for _ in range(M):
        u, v, c = map(int, input().split())
        adj_list[u-1].append((v-1, c))
        adj_list[v-1].append((u-1, c))
    
    min_energy = float('inf')
    
    for i in range(N):
        for v, w in adj_list[i]:
            energy = w**2 + alpha
            dist = dijkstra(adj_list, v, i)
            min_energy = min(min_energy, energy + dist)
    
    if min_energy == float('inf'):
        print("Poor girl")
    else:
        print(min_energy)

if __name__ == "__main__":
    main()
