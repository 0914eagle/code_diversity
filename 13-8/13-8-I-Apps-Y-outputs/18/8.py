
import sys
import heapq

class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

def dijkstra(graph, src):
    dist = [float('inf')] * len(graph)
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        u = heapq.heappop(heap)[1]
        for edge in graph[u]:
            v = edge.v
            if dist[v] > dist[u] + edge.weight:
                dist[v] = dist[u] + edge.weight
                heapq.heappush(heap, (dist[v], v))
    return dist

def kruskal(graph):
    mst = []
    dist = [float('inf')] * len(graph)
    for i in range(len(graph)):
        dist[i] = min(edge.weight for edge in graph[i])
    heap = [(dist[i], i) for i in range(len(graph))]
    heapq.heapify(heap)
    while heap and len(mst) < len(graph) - 1:
        _, u = heapq.heappop(heap)
        for edge in graph[u]:
            v = edge.v
            if dist[v] > edge.weight and v not in mst:
                mst.append(edge)
                dist[v] = edge.weight
                heapq.heappush(heap, (dist[v], v))
    return mst

def get_diameter(graph):
    dist = dijkstra(graph, 0)
    return max(dist)

def add_edges(graph, mst):
    edges = []
    for edge in mst:
        if edge.u not in edges:
            edges.append(edge.u)
        if edge.v not in edges:
            edges.append(edge.v)
    return edges

def get_output(edges):
    return [str(edge) for edge in edges]

def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u - 1].append(Edge(u - 1, v - 1, 1))
        graph[v - 1].append(Edge(v - 1, u - 1, 1))
    mst = kruskal(graph)
    edges = add_edges(graph, mst)
    print(get_diameter(graph))
    print('\n'.join(get_output(edges)))

if __name__ == '__main__':
    main()

