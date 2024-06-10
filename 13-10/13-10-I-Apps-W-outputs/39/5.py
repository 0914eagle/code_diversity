
def add_edge(graph, x, y):
    graph[x].append(y)
    graph[y].append(x)

def find_path(graph, start, end, k):
    queue = [(start, 0)]
    visited = set()
    while queue:
        node, count = queue.pop(0)
        if node == end and count == k:
            return True
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, count + 1))
    return False

def solve(graph, queries):
    for query in queries:
        x, y, a, b, k = query
        add_edge(graph, x, y)
        result = find_path(graph, a, b, k)
        print("YES" if result else "NO")

def main():
    n = int(input())
    graph = {i: [] for i in range(1, n + 1)}
    for i in range(n - 1):
        u, v = map(int, input().split())
        add_edge(graph, u, v)
    q = int(input())
    queries = []
    for i in range(q):
        x, y, a, b, k = map(int, input().split())
        queries.append((x, y, a, b, k))
    solve(graph, queries)

if __name__ == '__main__':
    main()

