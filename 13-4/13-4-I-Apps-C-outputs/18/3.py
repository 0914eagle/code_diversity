
import sys
input = sys.stdin.read()

def f1(N, points):
    # convert the input to a list of tuples
    points = [tuple(map(int, point.split())) for point in points]
    
    # create a graph with the given points as vertices
    graph = {point: set() for point in points}
    
    # add edges to the graph with the Manhattan distance as weight
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            point1, point2 = points[i], points[j]
            graph[point1].add((point2, abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])))
            graph[point2].add((point1, abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])))
    
    # find the minimum spanning tree using Kruskal's algorithm
    mst = []
    visited = set()
    while graph and len(mst) < len(points) - 1:
        # find the edge with the minimum weight
        current_edge = min(graph, key=lambda edge: graph[edge[0]][edge[1]])
        point1, point2 = current_edge
        if point1 in visited or point2 in visited:
            continue
        
        # add the edge to the MST
        mst.append(current_edge)
        visited.add(point1)
        visited.add(point2)
        
        # remove the edge from the graph
        graph[point1].remove(current_edge)
        graph[point2].remove(current_edge)
        if not graph[point1]:
            del graph[point1]
        if not graph[point2]:
            del graph[point2]
    
    # return the total weight of the MST
    return sum(weight for point1, weight in mst)

def f2(N, points):
    # convert the input to a list of tuples
    points = [tuple(map(int, point.split())) for point in points]
    
    # create a graph with the given points as vertices
    graph = {point: set() for point in points}
    
    # add edges to the graph with the Manhattan distance as weight
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            point1, point2 = points[i], points[j]
            graph[point1].add((point2, abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])))
            graph[point2].add((point1, abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])))
    
    # find the minimum spanning tree using Prim's algorithm
    mst = []
    visited = set()
    while graph and len(mst) < len(points) - 1:
        # find the vertex with the minimum distance to the MST
        current_vertex = min(graph, key=lambda vertex: min(graph[vertex], default=float('inf'))[1])
        if current_vertex in visited:
            continue
        
        # add the vertex to the MST
        mst.append(current_vertex)
        visited.add(current_vertex)
        
        # remove the vertex from the graph
        for neighbor, weight in list(graph[current_vertex]):
            if neighbor in visited:
                continue
            graph[neighbor].remove((current_vertex, weight))
            if not graph[neighbor]:
                del graph[neighbor]
    
    # return the total weight of the MST
    return sum(weight for point1, weight in mst)

if __name__ == '__main__':
    N = int(input())
    points = [input().strip() for _ in range(N)]
    print(f1(N, points))
    print(f2(N, points))

