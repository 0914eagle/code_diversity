
def bfs(graph, start):
    queue = [start]
    visited = set()
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
    return visited

def is_valid_bfs(graph, sequence):
    start = 1
    visited = set()
    for node in sequence:
        if node not in graph:
            return False
        if node == start:
            start = node
            continue
        if node in visited:
            return False
        visited.add(node)
    return True

def main():
    n = int(input())
    graph = {}
    for _ in range(n - 1):
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

