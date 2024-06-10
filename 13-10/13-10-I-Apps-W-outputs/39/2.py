
def find_path(graph, start, end, k, visited=None):
    if visited is None:
        visited = set()
    if start == end:
        return k == 0
    if start not in graph:
        return False
    for node in graph[start]:
        if node not in visited:
            visited.add(node)
            if find_path(graph, node, end, k-1, visited):
                return True
            visited.remove(node)
    return False

def solve(n, edges, queries):
    graph = {}
    for i in range(n):
        graph[i+1] = []
    for edge in edges:
        u, v = edge
        graph[u].append(v)
        graph[v].append(u)
    
    result = []
    for query in queries:
        x, y, a, b, k = query
        graph[x].append(y)
        graph[y].append(x)
        result.append("YES" if find_path(graph, a, b, k) else "NO")
        graph[x].remove(y)
        graph[y].remove(x)
    return result

def main():
    n, m = map(int, input().split())
    edges = []
    for i in range(m):
        edges.append(list(map(int, input().split())))
    q = int(input())
    queries = []
    for i in range(q):
        queries.append(list(map(int, input().split())))
    result = solve(n, edges, queries)
    for r in result:
        print(r)

if __name__ == '__main__':
    main()

