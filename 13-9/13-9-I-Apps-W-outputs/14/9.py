
def get_shortest_path(graph, start, end):
    visited = [False] * len(graph)
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        current = path[-1]

        if current == end:
            return path

        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(path + [neighbor])

    return []

def solve(n, m, roads):
    graph = [[] for _ in range(n)]

    for a, b, _ in roads:
        graph[a].append(b)
        graph[b].append(a)

    path = get_shortest_path(graph, 0, 1)

    if not path:
        return "impossible"

    return " ".join(str(p) for p in path)

def main():
    n, m = map(int, input().split())
    roads = []

    for _ in range(m):
        a, b, d = map(int, input().split())
        roads.append((a, b, d))

    print(solve(n, m, roads))

if __name__ == '__main__':
    main()

