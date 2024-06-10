
def read_input():
    n, m = map(int, input().split())
    roads = []
    for _ in range(m):
        a, b, d = map(int, input().split())
        roads.append((a, b, d))
    return n, m, roads

def find_route(n, m, roads):
    # Initialize a graph with n vertices and m edges
    graph = [[] for _ in range(n)]
    for a, b, d in roads:
        graph[a].append((b, d))
        graph[b].append((a, d))
    
    # Find the shortest path from Delft (vertex 0) to Amsterdam (vertex 1)
    visited = [False] * n
    queue = [(0, 0, [0])]
    while queue:
        dist, prev, path = queue.pop(0)
        current = path[-1]
        if current == 1:
            return path
        for neighbor, weight in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((dist + weight, neighbor, path + [neighbor]))
    
    return "impossible"

def main():
    n, m, roads = read_input()
    print(find_route(n, m, roads))

if __name__ == '__main__':
    main()

