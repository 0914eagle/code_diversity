
import sys
import collections

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, s):
        visited = [False] * self.vertices
        stack = []
        stack.append(s)

        while stack:
            node = stack.pop()
            if visited[node]:
                continue
            visited[node] = True
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)
        return visited

def get_escapable_pigs(graph, pigs):
    escapable_pigs = set()
    for pig in pigs:
        if graph.dfs(pig):
            escapable_pigs.add(pig)
    return escapable_pigs

def get_min_wolves(graph, pigs):
    escapable_pigs = get_escapable_pigs(graph, pigs)
    if len(escapable_pigs) == len(pigs):
        return 0

    min_wolves = sys.maxsize
    for pig in escapable_pigs:
        graph.remove_edge(pig, pig)
        min_wolves = min(min_wolves, get_min_wolves(graph, pigs))
        graph.add_edge(pig, pig)

    return min_wolves + 1

def main():
    vertices, pigs = map(int, input().split())
    graph = Graph(vertices)

    for _ in range(vertices-1):
        u, v = map(int, input().split())
        graph.add_edge(u, v)

    pigs = list(map(int, input().split()))
    print(get_min_wolves(graph, pigs))

if __name__ == '__main__':
    main()

