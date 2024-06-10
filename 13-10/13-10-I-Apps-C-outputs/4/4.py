
import sys
sys.setrecursionlimit(10000)

class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]
        self.visited = [False] * n
    
    def add_edge(self, u, v):
        self.adj[u].append(v)
    
    def dfs(self, s):
        if self.visited[s]:
            return
        self.visited[s] = True
        for v in self.adj[s]:
            self.dfs(v)

def get_min_time(n, m, logs):
    # Create a graph with n boulders and m logs
    g = Graph(n + m + 2)
    
    # Add edges between boulders and logs
    for u, v in logs:
        if u >= 0:
            g.add_edge(n + u, v + n)
        if v >= 0:
            g.add_edge(n + v, u + n)
    
    # Add edges between the left and right river banks
    g.add_edge(0, n)
    g.add_edge(n + m, n + m + 1)
    
    # Find the minimum time required to cross the river
    visited = [False] * (n + m + 2)
    min_time = 0
    for i in range(n + m + 2):
        if not visited[i]:
            visited[i] = True
            min_time += 1
            g.dfs(i)
    
    return min_time

def main():
    n, m, p = map(int, input().split())
    logs = []
    for _ in range(p):
        logs.append(list(map(int, input().split())))
    print(get_min_time(n, m, logs))

if __name__ == '__main__':
    main()

