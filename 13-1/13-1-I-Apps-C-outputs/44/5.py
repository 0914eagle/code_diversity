
def get_min_energy(N, M, alpha, roads):
    # Initialize a graph with N nodes and M edges
    graph = [[] for _ in range(N)]
    for u, v, c in roads:
        graph[u-1].append((v-1, c))
        graph[v-1].append((u-1, c))
    
    # Dijkstra's algorithm to find the shortest path between all pairs of nodes
    dist = [float('inf') for _ in range(N)]
    dist[0] = 0
    q = [(0, 0)]
    while q:
        u, dist_u = heapq.heappop(q)
        if dist_u > dist[u]:
            continue
        for v, c in graph[u]:
            dist_v = dist_u + c
            if dist_v < dist[v]:
                dist[v] = dist_v
                heapq.heappush(q, (v, dist_v))
    
    # Calculate the minimum energy needed to visit all nodes and return to the starting node
    min_energy = float('inf')
    for u in range(N):
        energy = dist[u]**2 + alpha * (len(graph[u]) - 1)
        min_energy = min(min_energy, energy)
    
    return min_energy

def main():
    N, M, alpha = map(int, input().split())
    roads = []
    for _ in range(M):
        u, v, c = map(int, input().split())
        roads.append((u, v, c))
    print(get_min_energy(N, M, alpha, roads))

if __name__ == '__main__':
    main()

