
import sys
input = sys.stdin.read()

def f1(points):
    # convert the input to a list of tuples
    points = [tuple(map(int, point.split())) for point in points.splitlines()]
    return points

def f2(points):
    # find the minimum spanning tree using Kruskal's algorithm
    mst = 0
    edges = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            edges.append((points[i], points[j], abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))
    edges.sort(key=lambda x: x[2])
    visited = set()
    for edge in edges:
        if edge[0] not in visited and edge[1] not in visited:
            visited.add(edge[0])
            visited.add(edge[1])
            mst += edge[2]
            if len(visited) == len(points):
                break
    return mst

if __name__ == '__main__':
    points = f1(input)
    print(f2(points))

