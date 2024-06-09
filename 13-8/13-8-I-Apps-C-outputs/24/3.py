
def minimum_spanning_tree(points):
    # Sort the points based on their x-coordinate
    sorted_points = sorted(points, key=lambda point: point[0])

    # Create a disjoint set data structure to store the points and their parents
    dsu = DisjointSetUnion(sorted_points)

    # Initialize the minimum spanning tree weight to 0
    mst_weight = 0

    # Iterate through the points and find the minimum spanning tree weight
    for i in range(len(sorted_points)):
        for j in range(i+1, len(sorted_points)):
            point1 = sorted_points[i]
            point2 = sorted_points[j]
            weight = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
            if dsu.find(point1) != dsu.find(point2):
                dsu.union(point1, point2)
                mst_weight += weight

    return mst_weight

# Disjoint Set Union (DSU) data structure
class DisjointSetUnion:
    def __init__(self, points):
        self.parents = {point: point for point in points}
        self.ranks = {point: 0 for point in points}

    def find(self, point):
        if self.parents[point] != point:
            self.parents[point] = self.find(self.parents[point])
        return self.parents[point]

    def union(self, point1, point2):
        root1 = self.find(point1)
        root2 = self.find(point2)
        if self.ranks[root1] > self.ranks[root2]:
            self.parents[root2] = root1
        elif self.ranks[root1] < self.ranks[root2]:
            self.parents[root1] = root2
        else:
            self.parents[root2] = root1
            self.ranks[root1] += 1

