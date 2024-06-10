
def read_input():
    A, H = map(int, input().split())
    n, m = map(int, input().split())
    passages = []
    for _ in range(m):
        e, b, a, h = map(int, input().split())
        passages.append((e, b, a, h))
    return A, H, n, m, passages

def find_safe_path(A, H, n, m, passages):
    # Initialize the graph with the passages
    graph = [[] for _ in range(n + 1)]
    for e, b, a, h in passages:
        graph[e].append((b, a, h))
    
    # Dijkstra's algorithm to find the shortest path
    queue = [(0, 1, A)]
    visited = set()
    while queue:
        dist, node, attack = heapq.heappop(queue)
        if node == n:
            return dist
        if node in visited:
            continue
        visited.add(node)
        for neighbor, neighbor_attack, neighbor_health in graph[node]:
            if neighbor_health <= attack:
                heapq.heappush(queue, (dist + 1, neighbor, attack - neighbor_attack))
    
    return -1

def solve(A, H, n, m, passages):
    # Find the shortest path
    dist = find_safe_path(A, H, n, m, passages)
    if dist == -1:
        return "Oh no"
    
    # Calculate the maximum health Unnar can have after getting through the cave-system
    max_health = H
    for _ in range(dist):
        max_health -= passages[n - 1][2]
        if max_health <= 0:
            return "Oh no"
    
    return max_health

if __name__ == '__main__':
    A, H, n, m, passages = read_input()
    print(solve(A, H, n, m, passages))

