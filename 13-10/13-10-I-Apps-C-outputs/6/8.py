
def find_max_health(A, H, n, m, passages):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n + 1)]
    for e, b, a, h in passages:
        graph[e].append((b, a, h))
    
    # Dijkstra's algorithm to find the shortest path from node 1 to node n
    visited = [False] * (n + 1)
    queue = [(0, 1, A)]
    while queue:
        dist, node, attack = heapq.heappop(queue)
        if node == n:
            return dist
        if visited[node]:
            continue
        visited[node] = True
        for neighbor, a, h in graph[node]:
            heapq.heappush(queue, (dist + h, neighbor, attack - a))
    
    return -1

def main():
    A, H = map(int, input().split())
    n, m = map(int, input().split())
    passages = []
    for _ in range(m):
        e, b, a, h = map(int, input().split())
        passages.append((e, b, a, h))
    print(find_max_health(A, H, n, m, passages))

if __name__ == '__main__':
    main()

