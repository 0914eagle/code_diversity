
def is_leaf(graph, vertex):
    return len(graph[vertex]) == 1

def bfs(graph, source, visited):
    queue = [source]
    visited[source] = True
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    return visited

def find_min_wolves(graph, pigs):
    visited = [False] * len(graph)
    for pig in pigs:
        bfs(graph, pig, visited)
    return len([vertex for vertex, visited in enumerate(visited) if visited and is_leaf(graph, vertex)])

def main():
    v, p = map(int, input().split())
    graph = [[] for _ in range(v)]
    for _ in range(v - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    pigs = list(map(int, input().split()))
    print(find_min_wolves(graph, pigs))

if __name__ == '__main__':
    main()

