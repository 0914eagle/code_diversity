
def get_connected_colors(graph, u, v):
    visited = set()
    queue = [u]
    while queue:
        node = queue.pop(0)
        if node == v:
            return visited
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append(c)
        graph[b].append(c)
    q = int(input())
    for _ in range(q):
        u, v = map(int, input().split())
        print(len(get_connected_colors(graph, u, v)))

if __name__ == '__main__':
    main()

