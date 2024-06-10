
def bfs(graph, start):
    queue = [start]
    visited = set()
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex])
    return visited

def is_valid_bfs(graph, sequence):
    visited = set()
    for vertex in sequence:
        if vertex not in graph:
            return False
        if vertex in visited:
            return False
        visited.add(vertex)
    return True

def main():
    n = int(input())
    graph = {}
    for i in range(n - 1):
        x, y = map(int, input().split())
        if x not in graph:
            graph[x] = []
        if y not in graph:
            graph[y] = []
        graph[x].append(y)
        graph[y].append(x)
    sequence = list(map(int, input().split()))
    if is_valid_bfs(graph, sequence):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()

