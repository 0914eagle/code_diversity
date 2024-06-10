
import sys
sys.setrecursionlimit(10000)

def get_graph(P, R, L):
    graph = {}
    for i in range(R):
        graph[i] = []
    for i in range(L):
        edge = list(map(int, input().split()))
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph

def bfs(graph, start, end):
    queue = [start]
    visited = set()
    while queue:
        node = queue.pop(0)
        if node == end:
            return True
        if node not in visited:
            visited.add(node)
            queue += graph[node]
    return False

def solve(P, R, L):
    graph = get_graph(P, R, L)
    start = -2
    end = -1
    if bfs(graph, start, end):
        return P
    else:
        return -1

def main():
    P, R, L = map(int, input().split())
    print(solve(P, R, L))

if __name__ == '__main__':
    main()

