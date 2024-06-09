
import sys
input = sys.stdin.read()

def f1(points):
    # Calculate the Manhattan distance between each pair of points
    distances = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distances.append((points[i][0]-points[j][0])+(points[i][1]-points[j][1]))
    
    # Sort the distances in ascending order
    distances.sort()
    
    # Return the sum of the first (N-1) distances, which is the weight of the minimum spanning tree
    return sum(distances[:len(points)-1])

def f2(points):
    # Use Kruskal's algorithm to find the minimum spanning tree
    mst = []
    visited = set()
    for i in range(len(points)):
        if i not in visited:
            visited.add(i)
            for j in range(i+1, len(points)):
                if j not in visited:
                    if (points[i][0]-points[j][0])+(points[i][1]-points[j][1]) == distances[0]:
                        mst.append((i, j))
                        visited.add(j)
                        break
    
    # Return the sum of the weights of the edges in the minimum spanning tree
    return sum(distances[i] for i in range(len(mst)))

if __name__ == '__main__':
    points = []
    for line in input.splitlines():
        x, y = map(int, line.split())
        points.append((x, y))
    print(f1(points))
    print(f2(points))

