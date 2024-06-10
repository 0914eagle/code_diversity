
def solve(A, H, n, m, passages):
    # Initialize a graph to represent the cave-system
    graph = {i: set() for i in range(1, n + 1)}

    # Add the passages to the graph
    for e, b, a, h in passages:
        graph[e].add((b, a, h))

    # Dijkstra's algorithm to find the shortest path from area 1 to area n
    visited = set()
    queue = [(0, 1, A)]
    while queue:
        cost, curr, attack_points = heapq.heappop(queue)
        if curr == n:
            return cost
        if curr in visited:
            continue
        visited.add(curr)
        for next_area, next_attack_points, next_health_points in graph[curr]:
            heapq.heappush(queue, (cost + 1, next_area, attack_points - next_attack_points))

    return -1

def main():
    A, H = map(int, input().split())
    n, m = map(int, input().split())
    passages = []
    for _ in range(m):
        e, b, a, h = map(int, input().split())
        passages.append((e, b, a, h))
    print(solve(A, H, n, m, passages))

if __name__ == '__main__':
    main()

