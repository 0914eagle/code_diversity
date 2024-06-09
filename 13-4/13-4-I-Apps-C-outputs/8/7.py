
def get_shortest_path(graph, start, end):
    visited = set()
    queue = [(start, 0)]

    while queue:
        (vertex, distance) = queue.pop(0)

        if vertex not in visited:
            visited.add(vertex)

            if vertex == end:
                return distance

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, distance + 1))

    return -1

def f1(n, A, B):
    graph = {}

    for i in range(n):
        graph[i] = []

    for i in range(n):
        l, r, t = map(int, input().split())

        if l != -1:
            graph[i].append(l)

        if r != -1:
            graph[i].append(r)

    return get_shortest_path(graph, A, B)

def f2(...):
    ...

if __name__ == '__main__':
    n, A, B = map(int, input().split())
    print(f1(n, A, B))

