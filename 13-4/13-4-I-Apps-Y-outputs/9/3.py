
import sys
import heapq

class DisjointSet:
    def __init__(self, n):
        self.parents = [-1] * n
        self.ranks = [0] * n
        self.n = n
    
    def find_set(self, x):
        if self.parents[x] == -1:
            return x
        else:
            self.parents[x] = self.find_set(self.parents[x])
            return self.parents[x]
    
    def union_sets(self, x, y):
        x_root = self.find_set(x)
        y_root = self.find_set(y)
        if x_root == y_root:
            return
        if self.ranks[x_root] > self.ranks[y_root]:
            self.parents[y_root] = x_root
        elif self.ranks[x_root] < self.ranks[y_root]:
            self.parents[x_root] = y_root
        else:
            self.parents[y_root] = x_root
            self.ranks[x_root] += 1
    
    def is_same_set(self, x, y):
        return self.find_set(x) == self.find_set(y)

def dijkstra(graph, start, end):
    visited = [False] * len(graph)
    distances = [float('inf')] * len(graph)
    previous = [None] * len(graph)
    pq = [(0, start)]
    visited[start] = True
    distances[start] = 0
    while len(pq) > 0:
        (dist, node) = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        if node == end:
            break
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = node
                    heapq.heappush(pq, (new_dist, neighbor))
    return distances, previous

def solve(n, m, k, roads, routes):
    graph = [[] for _ in range(n + 1)]
    for (u, v, w) in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))
    disjoint_set = DisjointSet(n + 1)
    for (u, v) in routes:
        disjoint_set.union_sets(u, v)
    cost = 0
    for i in range(1, n + 1):
        if disjoint_set.find_set(i) == disjoint_set.find_set(1):
            continue
        distances, previous = dijkstra(graph, 1, i)
        cost += distances[i]
    return cost

n, m, k = map(int, input().split())
roads = []
for _ in range(m):
    x, y, w = map(int, input().split())
    roads.append((x, y, w))
routes = []
for _ in range(k):
    a, b = map(int, input().split())
    routes.append((a, b))
print(solve(n, m, k, roads, routes))

