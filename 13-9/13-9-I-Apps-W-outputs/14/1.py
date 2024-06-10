
def get_shortest_path(graph, start, end):
    visited = set()
    queue = [[start]]

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node not in visited:
            visited.add(node)
            neighbors = graph[node]

            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == end:
                    return new_path

    return None

def solve(n, m, roads):
    graph = {}

    for road in roads:
        a, b, d = road
        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    path = get_shortest_path(graph, 0, 1)

    if path is None:
        return "impossible"

    return " ".join(str(node) for node in path[1:])

def main():
    n, m = map(int, input().split())
    roads = []

    for _ in range(m):
        a, b, d = map(int, input().split())
        roads.append((a, b, d))

    print(solve(n, m, roads))

if __name__ == '__main__':
    main()

