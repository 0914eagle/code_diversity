
import sys
sys.setrecursionlimit(10000)

def get_edges(n_vertices, edges):
    graph = {}
    for edge in edges:
        u, v = edge[0], edge[1]
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
    
    return graph

def bfs(graph, start, visited):
    queue = [start]
    visited[start] = True
    
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return visited

def solve(n_vertices, n_pigs, edges, pigs):
    graph = get_edges(n_vertices, edges)
    visited = [False] * n_vertices
    for pig in pigs:
        bfs(graph, pig, visited)
    
    return n_vertices - sum(visited)

def main():
    n_vertices, n_pigs = map(int, input().split())
    edges = []
    for _ in range(n_vertices - 1):
        edges.append(list(map(int, input().split())))
    pigs = list(map(int, input().split()))
    print(solve(n_vertices, n_pigs, edges, pigs))

if __name__ == '__main__':
    main()

