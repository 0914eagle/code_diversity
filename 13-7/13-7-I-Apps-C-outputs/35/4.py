
def get_shortest_path(graph, start, end):
    visited = [False] * len(graph)
    queue = [start]
    parent = [-1] * len(graph)
    while queue:
        node = queue.pop(0)
        if node == end:
            break
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                parent[neighbor] = node
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = parent[current]
    return path[::-1]

def count_ways(graph, n):
    pairs = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            pairs.append((i, j))
    count = 0
    for pair in pairs:
        path = get_shortest_path(graph, pair[0], pair[1])
        flag = True
        for edge in path:
            if edge not in graph[pair[0]]:
                flag = False
                break
        if flag:
            count += 1
    return count % 1000000007

def main():
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    print(count_ways(graph, n))

if __name__ == '__main__':
    main()

