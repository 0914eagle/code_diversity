
def f1(n, A, B):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the input
    for i in range(n):
        graph[i].append((A, i))
        graph[i].append((B, i))

    # Find the shortest path between A and B using BFS
    queue = [(A, [A])]
    visited = set()
    while queue:
        node, path = queue.pop(0)
        if node == B:
            return len(path) - 1
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor[0] not in visited:
                    queue.append((neighbor[0], path + [neighbor[0]]))

    # If there is no path between A and B, return -1
    return -1

def f2(n, A, B):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the input
    for i in range(n):
        graph[i].append((A, i))
        graph[i].append((B, i))

    # Find the shortest path between A and B using Dijkstra's algorithm
    dist = [float('inf') for _ in range(n)]
    dist[A] = 0
    queue = [(0, A)]
    while queue:
        cost, node = heapq.heappop(queue)
        if node == B:
            return cost
        if dist[node] < cost:
            continue
        for neighbor in graph[node]:
            new_cost = cost + 1
            if new_cost < dist[neighbor[0]]:
                dist[neighbor[0]] = new_cost
                heapq.heappush(queue, (new_cost, neighbor[0]))

    # If there is no path between A and B, return -1
    return -1

if __name__ == '__main__':
    n, A, B = map(int, input().split())
    print(f1(n, A, B))
    print(f2(n, A, B))

