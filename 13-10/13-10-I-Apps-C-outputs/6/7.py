
def get_maximum_health(A, H, n, m, passages):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n + 1)]
    for e, b, a, h in passages:
        graph[e].append((b, a, h))
    
    # Dijkstra's algorithm to find the shortest path from node 1 to node n
    visited = [False] * (n + 1)
    queue = [(0, 1, H)]
    while queue:
        dist, node, health = heapq.heappop(queue)
        if visited[node]:
            continue
        visited[node] = True
        if node == n:
            return health
        for neighbor, attack, health_loss in graph[node]:
            heapq.heappush(queue, (dist + 1, neighbor, max(0, health - attack + health_loss)))
    
    return -1

def solve(A, H, n, m, passages):
    # Find the shortest path from node 1 to node n
    health = get_maximum_health(A, H, n, m, passages)
    
    # If there is no path, return 'Oh no'
    if health == -1:
        return 'Oh no'
    
    # Otherwise, return the maximum health Unnar can have after getting through the cave-system
    return health

if __name__ == '__main__':
    A, H, n, m = map(int, input().split())
    passages = []
    for _ in range(m):
        e, b, a, h = map(int, input().split())
        passages.append((e, b, a, h))
    print(solve(A, H, n, m, passages))

