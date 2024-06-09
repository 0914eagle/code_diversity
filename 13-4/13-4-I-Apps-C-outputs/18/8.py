
import sys
input = sys.stdin.read()

def f1(points):
    # Calculate the Manhattan distance between all pairs of points
    distances = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distances.append((points[i], points[j], abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])))
    
    # Sort the distances in ascending order
    distances.sort(key=lambda x: x[2])
    
    # Initialize the minimum spanning tree with the first two points
    mst = [distances[0][:2]]
    
    # Add the remaining points to the minimum spanning tree
    for distance in distances[1:]:
        if distance[0] in mst or distance[1] in mst:
            mst.append(distance[:2])
    
    # Calculate the total weight of the minimum spanning tree
    total_weight = 0
    for edge in mst:
        total_weight += edge[2]
    
    return total_weight

def f2(points):
    # Calculate the Manhattan distance between all pairs of points
    distances = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distances.append((points[i], points[j], abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])))
    
    # Sort the distances in ascending order
    distances.sort(key=lambda x: x[2])
    
    # Initialize the minimum spanning tree with the first two points
    mst = [distances[0][:2]]
    
    # Add the remaining points to the minimum spanning tree
    for distance in distances[1:]:
        if distance[0] in mst or distance[1] in mst:
            mst.append(distance[:2])
    
    # Calculate the total weight of the minimum spanning tree
    total_weight = 0
    for edge in mst:
        total_weight += edge[2]
    
    return total_weight

if __name__ == '__main__':
    points = []
    for line in input.splitlines():
        x, y = map(int, line.split())
        points.append((x, y))
    print(f1(points))
    print(f2(points))

