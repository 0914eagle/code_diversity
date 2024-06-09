
import sys

def f1(points):
    # Calculate the Manhattan distance between all pairs of points
    distances = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distances.append((points[i], points[j], abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))
    
    # Sort the distances in ascending order
    distances.sort(key=lambda x: x[2])
    
    # Initialize the minimum spanning tree with the first point
    mst = [distances[0][0]]
    
    # Iterate through the remaining distances and add the point with the minimum distance to the MST
    for distance in distances[1:]:
        if distance[0] in mst or distance[1] in mst:
            continue
        mst.append(distance[0] if distance[0] not in mst else distance[1])
    
    # Return the weight of the minimum spanning tree
    return sum(distance[2] for distance in distances if distance[0] in mst and distance[1] in mst)

def f2(points):
    # Calculate the Manhattan distance between all pairs of points
    distances = []
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            distances.append((points[i], points[j], abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])))
    
    # Sort the distances in ascending order
    distances.sort(key=lambda x: x[2])
    
    # Initialize the minimum spanning tree with the first point
    mst = [distances[0][0]]
    
    # Iterate through the remaining distances and add the point with the minimum distance to the MST
    for distance in distances[1:]:
        if distance[0] in mst or distance[1] in mst:
            continue
        mst.append(distance[0] if distance[0] not in mst else distance[1])
    
    # Return the weight of the minimum spanning tree
    return sum(distance[2] for distance in distances if distance[0] in mst and distance[1] in mst)

if __name__ == '__main__':
    points = []
    for _ in range(int(input())):
        points.append(tuple(map(int, input().split())))
    print(f1(points))
    print(f2(points))

