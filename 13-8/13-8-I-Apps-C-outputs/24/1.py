
def minimum_spanning_tree(points):
    # Sort the points based on their x-coordinate
    sorted_points = sorted(points, key=lambda point: point[0])

    # Create a disjoint set data structure to store the points and their parents
    dsu = DisjointSetUnion(sorted_points)

    # Initialize the minimum spanning tree weight to 0
    mst_weight = 0

    # Iterate through the points and add the weight of the edges to the minimum spanning tree weight
    for i in range(len(sorted_points)):
        for j in range(i + 1, len(sorted_points)):
            point1 = sorted_points[i]
            point2 = sorted_points[j]
            weight = manhattan_distance(point1, point2)
            if dsu.find(point1) != dsu.find(point2):
                mst_weight += weight
                dsu.union(point1, point2)

    return mst_weight

def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def read_points(n):
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append((x, y))
    return points

def main():
    n = int(input())
    points = read_points(n)
    print(minimum_spanning_tree(points))

if __name__ == "__main__":
    main()

