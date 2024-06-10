
def get_graph(L, R):
    graph = {}
    for i in range(-2, R):
        graph[i] = set()
    for i in range(L):
        e1, e2 = map(int, input().split())
        graph[e1].add(e2)
        graph[e2].add(e1)
    return graph

def bfs(graph, start, end):
    queue = [(start, 0)]
    visited = set()
    while queue:
        node, time = queue.pop(0)
        if node == end:
            return time
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, time + 1))
    return -1

def solve(P, R, L):
    graph = get_graph(L, R)
    time = 0
    for i in range(P):
        time += bfs(graph, -2, 0)
        graph = get_graph(L, R)
    return time

if __name__ == '__main__':
    P, R, L = map(int, input().split())
    print(solve(P, R, L))

