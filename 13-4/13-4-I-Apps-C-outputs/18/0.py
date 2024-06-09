
import sys
import heapq

class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w

def f1(N, points):
    # create a graph with N nodes and 0 edges
    graph = [[] for _ in range(N)]

    # add edges to the graph
    for i in range(N):
        for j in range(i+1, N):
            w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            graph[i].append(Edge(i, j, w))
            graph[j].append(Edge(j, i, w))

    return graph

def f2(graph):
    # use Kruskal's algorithm to find the minimum spanning tree
    mst = []
    visited = set()
    for edge in heapq.merge(*graph):
        if edge.u not in visited and edge.v not in visited:
            mst.append(edge)
            visited.add(edge.u)
            visited.add(edge.v)
            if len(visited) == len(graph):
                break

    # calculate the total weight of the minimum spanning tree
    total_weight = 0
    for edge in mst:
        total_weight += edge.w

    return total_weight

if __name__ == '__main__':
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))

    graph = f1(N, points)
    total_weight = f2(graph)

    print(total_weight)

