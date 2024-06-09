
def f1(n, A, B):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the input
    for i in range(n):
        graph[i].append((A, 1))
        graph[i].append((B, 1))

    # Find the shortest path between A and B using BFS
    queue = [(A, 0)]
    visited = set()
    while queue:
        node, distance = queue.pop(0)
        if node == B:
            return distance
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + weight))

    # If no path is found, return -1
    return -1

def f2(n, A, B):
    # Initialize a graph with n nodes and no edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the input
    for i in range(n):
        graph[i].append((A, 1))
        graph[i].append((B, 1))

    # Find the shortest path between A and B using Dijkstra's algorithm
    visited = set()
    queue = [(0, A)]
    while queue:
        distance, node = heapq.heappop(queue)
        if node == B:
            return distance
        if node not in visited:
            visited.add(node)
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (distance + weight, neighbor))

    # If no path is found, return -1
    return -1

if __name__ == '__main__':
    n, A, B = map(int, input().split())
    print(f1(n, A, B))
    print(f2(n, A, B))

