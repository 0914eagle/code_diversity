
def f1(n, m, edges):
    # create a graph with the given edges
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # find all pairs of towns that are connected by a railway
    railway_pairs = set()
    for u in range(1, n + 1):
        for v in graph[u]:
            if u < v:
                railway_pairs.add((u, v))
    
    # find all pairs of towns that are connected by a road
    road_pairs = set()
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            if (u, v) not in railway_pairs:
                road_pairs.add((u, v))
    
    # find the shortest path from town 1 to town n using only railways
    dist = [float('inf') for _ in range(n + 1)]
    dist[1] = 0
    queue = [(1, 0)]
    while queue:
        u, d = queue.pop(0)
        for v in graph[u]:
            if d + 1 < dist[v]:
                dist[v] = d + 1
                queue.append((v, d + 1))
    
    # find the shortest path from town 1 to town n using only roads
    dist_road = [float('inf') for _ in range(n + 1)]
    dist_road[1] = 0
    queue = [(1, 0)]
    while queue:
        u, d = queue.pop(0)
        for v in graph[u]:
            if d + 1 < dist_road[v] and (u, v) in road_pairs:
                dist_road[v] = d + 1
                queue.append((v, d + 1))
    
    # find the maximum of the shortest paths from town 1 to town n using only railways and only roads
    max_dist = max(dist[n], dist_road[n])
    
    return max_dist

def f2(...):
    # code for function 2 here
    pass

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    print(f1(n, m, edges))

