
def get_graph(R, L, edges):
    graph = {}
    for i in range(-2, R):
        graph[i] = []
    for e1, e2 in edges:
        graph[e1].append(e2)
        graph[e2].append(e1)
    return graph

def bfs(graph, start, end):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node == end:
            return True
        if node not in visited:
            visited.add(node)
            queue += graph[node]
    return False

def solve(P, R, L, edges):
    graph = get_graph(R, L, edges)
    start = -2
    end = -1
    if bfs(graph, start, end):
        return 0
    else:
        return -1

def main():
    P, R, L = map(int, input().split())
    edges = []
    for i in range(L):
        e1, e2 = map(int, input().split())
        edges.append((e1, e2))
    print(solve(P, R, L, edges))

if __name__ == '__main__':
    main()

